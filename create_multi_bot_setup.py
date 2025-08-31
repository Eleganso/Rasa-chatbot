#!/usr/bin/env python3
"""
Multi-Bot Setup for 5 different business bots
"""

import os
import shutil
import yaml
from datetime import datetime

def create_bot_structure():
    """Create structure for 5 different bots"""
    
    bots = {
        'tourism_bot': {
            'port': 5001,
            'name': 'TourismBot',
            'description': 'Туристически съвети за България',
            'intents': ['ask_attractions', 'ask_hotels', 'ask_transport', 'ask_food', 'ask_weather']
        },
        'tech_support_bot': {
            'port': 5002,
            'name': 'TechSupportBot', 
            'description': 'Техническа поддръжка',
            'intents': ['ask_installation', 'ask_troubleshooting', 'ask_features', 'ask_pricing', 'ask_contact']
        },
        'sales_bot': {
            'port': 5003,
            'name': 'SalesBot',
            'description': 'Продажби и консултации',
            'intents': ['ask_products', 'ask_pricing', 'ask_demo', 'ask_quote', 'ask_contact']
        },
        'hr_bot': {
            'port': 5004,
            'name': 'HRBot',
            'description': 'HR помощник',
            'intents': ['ask_jobs', 'ask_benefits', 'ask_application', 'ask_company', 'ask_culture']
        },
        'customer_service_bot': {
            'port': 5005,
            'name': 'CustomerServiceBot',
            'description': 'Клиентски сервиз',
            'intents': ['ask_order', 'ask_refund', 'ask_shipping', 'ask_complaint', 'ask_help']
        }
    }
    
    for bot_name, config in bots.items():
        print(f"Creating {bot_name}...")
        
        # Create bot directory
        bot_dir = f"bots/{bot_name}"
        os.makedirs(bot_dir, exist_ok=True)
        
        # Create Rasa structure
        rasa_dir = f"{bot_dir}/rasa"
        os.makedirs(f"{rasa_dir}/data", exist_ok=True)
        os.makedirs(f"{rasa_dir}/models", exist_ok=True)
        
        # Create config files
        create_bot_config(bot_name, config, rasa_dir)
        
        # Create start script
        create_start_script(bot_name, config)
        
        # Create web interface
        create_web_interface(bot_name, config)
    
    # Create main dashboard
    create_dashboard(bots)
    
    print("✅ All bots created successfully!")

def create_bot_config(bot_name, config, rasa_dir):
    """Create basic Rasa configuration for a bot"""
    
    # Create domain.yml
    domain_content = f"""version: "3.1"

intents:
  - greet
  - goodbye
  - {config['intents'][0]}
  - {config['intents'][1]}
  - {config['intents'][2]}
  - {config['intents'][3]}
  - {config['intents'][4]}

entities:
  - name
  - location

slots:
  name:
    type: text
    mappings:
    - type: from_entity
      entity: name
  location:
    type: text
    mappings:
    - type: from_entity
      entity: location

responses:
  utter_greet:
  - text: "Здравей! Аз съм {config['name']}, {config['description']}. Как мога да ти помогна?"

  utter_goodbye:
  - text: "Довиждане! Радвам се, че успях да помогна!"

  utter_{config['intents'][0]}:
  - text: "Относно {config['intents'][0]} - това е демо отговор. В реален бот тук ще има конкретна информация."

  utter_{config['intents'][1]}:
  - text: "Относно {config['intents'][1]} - това е демо отговор. В реален бот тук ще има конкретна информация."

  utter_{config['intents'][2]}:
  - text: "Относно {config['intents'][2]} - това е демо отговор. В реален бот тук ще има конкретна информация."

  utter_{config['intents'][3]}:
  - text: "Относно {config['intents'][3]} - това е демо отговор. В реален бот тук ще има конкретна информация."

  utter_{config['intents'][4]}:
  - text: "Относно {config['intents'][4]} - това е демо отговор. В реален бот тук ще има конкретна информация."

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true
"""
    
    with open(f"{rasa_dir}/domain.yml", 'w', encoding='utf-8') as f:
        f.write(domain_content)
    
    # Create nlu.yml
    nlu_content = f"""version: "3.1"

nlu:
- intent: greet
  examples: |
    - здравей
    - здрасти
    - привет
    - добър ден
    - хей

- intent: goodbye
  examples: |
    - довиждане
    - чао
    - до скоро
    - лека

- intent: {config['intents'][0]}
  examples: |
    - {config['intents'][0]}
    - въпрос за {config['intents'][0]}
    - искам да знам за {config['intents'][0]}

- intent: {config['intents'][1]}
  examples: |
    - {config['intents'][1]}
    - въпрос за {config['intents'][1]}
    - искам да знам за {config['intents'][1]}

- intent: {config['intents'][2]}
  examples: |
    - {config['intents'][2]}
    - въпрос за {config['intents'][2]}
    - искам да знам за {config['intents'][2]}

- intent: {config['intents'][3]}
  examples: |
    - {config['intents'][3]}
    - въпрос за {config['intents'][3]}
    - искам да знам за {config['intents'][3]}

- intent: {config['intents'][4]}
  examples: |
    - {config['intents'][4]}
    - въпрос за {config['intents'][4]}
    - искам да знам за {config['intents'][4]}
"""
    
    with open(f"{rasa_dir}/data/nlu.yml", 'w', encoding='utf-8') as f:
        f.write(nlu_content)
    
    # Create stories.yml
    stories_content = f"""version: "3.1"

stories:
- story: greet and ask
  steps:
  - intent: greet
  - action: utter_greet
  - intent: {config['intents'][0]}
  - action: utter_{config['intents'][0]}

- story: direct question
  steps:
  - intent: {config['intents'][1]}
  - action: utter_{config['intents'][1]}

- story: goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye
"""
    
    with open(f"{rasa_dir}/data/stories.yml", 'w', encoding='utf-8') as f:
        f.write(stories_content)

def create_start_script(bot_name, config):
    """Create start script for each bot"""
    
    script_content = f"""@echo off
echo =========================================
echo    Starting {config['name']}
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Starting {config['name']} server...
echo Starting {config['name']} server on port {config['port']}...
start "{config['name']} Server" cmd /k "docker run --rm -v "%cd%\\bots\\{bot_name}\\rasa:/app" -p {config['port']}:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005"

echo.
echo Waiting for {config['name']} to start...
timeout /t 15 /nobreak >nul

echo.
echo Step 3: Opening {config['name']} chat interface...
start "" "bots\\{bot_name}\\web\\index.html"

echo.
echo =========================================
echo    {config['name']} Ready!
echo =========================================
echo.
echo ✅ {config['name']} server is running on http://localhost:{config['port']}
echo ✅ {config['name']} chat interface opened in your browser
echo ✅ {config['description']}
echo.
echo Chat interface location:
echo   bots\\{bot_name}\\web\\index.html
echo.
echo Enjoy testing {config['name']}! 🎉
echo.
pause
"""
    
    with open(f"start_{bot_name}.bat", 'w', encoding='utf-8') as f:
        f.write(script_content)

def create_web_interface(bot_name, config):
    """Create web interface for each bot"""
    
    web_dir = f"bots/{bot_name}/web"
    os.makedirs(web_dir, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{config['name']} - {config['description']}</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        
        .header {{
            text-align: center;
            color: white;
            margin-bottom: 20px;
        }}
        
        .header h1 {{
            margin: 0;
            font-size: 2.5em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .header p {{
            margin: 10px 0 0 0;
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .chat-container {{
            flex: 1;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        
        .chat-header {{
            background: #4CAF50;
            color: white;
            padding: 15px 20px;
            text-align: center;
            font-weight: bold;
        }}
        
        .chat-messages {{
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            background: #f8f9fa;
        }}
        
        .message {{
            margin-bottom: 15px;
            display: flex;
        }}
        
        .message.user {{
            justify-content: flex-end;
        }}
        
        .message.bot {{
            justify-content: flex-start;
        }}
        
        .message-content {{
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 18px;
            word-wrap: break-word;
        }}
        
        .message.user .message-content {{
            background: #007bff;
            color: white;
        }}
        
        .message.bot .message-content {{
            background: white;
            color: #333;
            border: 1px solid #e0e0e0;
        }}
        
        .chat-input {{
            padding: 20px;
            background: white;
            border-top: 1px solid #e0e0e0;
            display: flex;
            gap: 10px;
        }}
        
        .chat-input input {{
            flex: 1;
            padding: 12px 16px;
            border: 2px solid #e0e0e0;
            border-radius: 25px;
            font-size: 16px;
            outline: none;
            transition: border-color 0.3s;
        }}
        
        .chat-input input:focus {{
            border-color: #4CAF50;
        }}
        
        .chat-input button {{
            padding: 12px 24px;
            background: #4CAF50;
            color: white;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            font-size: 16px;
            transition: background 0.3s;
        }}
        
        .chat-input button:hover {{
            background: #45a049;
        }}
        
        .typing-indicator {{
            display: none;
            padding: 12px 16px;
            background: white;
            border: 1px solid #e0e0e0;
            border-radius: 18px;
            color: #666;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 {config['name']}</h1>
        <p>{config['description']}</p>
    </div>
    
    <div class="chat-container">
        <div class="chat-header">
            💬 Чат с {config['name']}
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <div class="message-content">
                    Здравей! Аз съм {config['name']}, {config['description']}. Как мога да ти помогна?
                </div>
            </div>
        </div>
        
        <div class="typing-indicator" id="typingIndicator">
            {config['name']} пише...
        </div>
        
        <div class="chat-input">
            <input type="text" id="messageInput" placeholder="Напишете вашето съобщение..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Изпрати</button>
        </div>
    </div>

    <script>
        const API_URL = 'http://localhost:{config['port']}/webhooks/rest/webhook';
        const chatMessages = document.getElementById('chatMessages');
        const messageInput = document.getElementById('messageInput');
        const typingIndicator = document.getElementById('typingIndicator');
        
        function addMessage(content, isUser = false) {{
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${{isUser ? 'user' : 'bot'}}`;
            
            const messageContent = document.createElement('div');
            messageContent.className = 'message-content';
            messageContent.textContent = content;
            
            messageDiv.appendChild(messageContent);
            chatMessages.appendChild(messageDiv);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }}
        
        function showTypingIndicator() {{
            typingIndicator.style.display = 'block';
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }}
        
        function hideTypingIndicator() {{
            typingIndicator.style.display = 'none';
        }}
        
        async function sendMessage() {{
            const message = messageInput.value.trim();
            if (!message) return;
            
            // Add user message
            addMessage(message, true);
            messageInput.value = '';
            
            // Show typing indicator
            showTypingIndicator();
            
            try {{
                const response = await fetch(API_URL, {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json',
                    }},
                    body: JSON.stringify({{
                        sender: 'user',
                        message: message
                    }})
                }});
                
                const data = await response.json();
                hideTypingIndicator();
                
                // Add bot response
                if (data && data.length > 0) {{
                    data.forEach(item => {{
                        if (item.text) {{
                            addMessage(item.text);
                        }}
                    }});
                }} else {{
                    addMessage('Съжалявам, не разбрах вашето съобщение. Моля, опитайте отново.');
                }}
                
            }} catch (error) {{
                hideTypingIndicator();
                addMessage('Грешка при свързване с бота. Моля, проверете дали сървърът работи.');
                console.error('Error:', error);
            }}
        }}
        
        function handleKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendMessage();
            }}
        }}
        
        // Focus on input when page loads
        messageInput.focus();
    </script>
</body>
</html>
"""
    
    with open(f"{web_dir}/index.html", 'w', encoding='utf-8') as f:
        f.write(html_content)

def create_dashboard(bots):
    """Create main dashboard to access all bots"""
    
    dashboard_content = """<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🤖 Multi-Bot Demo Dashboard</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        
        .header {
            text-align: center;
            color: white;
            margin-bottom: 40px;
        }
        
        .header h1 {
            margin: 0;
            font-size: 3em;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .header p {
            margin: 10px 0 0 0;
            font-size: 1.3em;
            opacity: 0.9;
        }
        
        .bots-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .bot-card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s, box-shadow 0.3s;
            cursor: pointer;
        }
        
        .bot-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        
        .bot-icon {
            font-size: 3em;
            text-align: center;
            margin-bottom: 15px;
        }
        
        .bot-name {
            font-size: 1.5em;
            font-weight: bold;
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }
        
        .bot-description {
            color: #666;
            text-align: center;
            margin-bottom: 20px;
            line-height: 1.5;
        }
        
        .bot-port {
            background: #4CAF50;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
            text-align: center;
            margin-bottom: 15px;
        }
        
        .bot-button {
            width: 100%;
            padding: 12px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        
        .bot-button:hover {
            background: #0056b3;
        }
        
        .footer {
            text-align: center;
            color: white;
            margin-top: 40px;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🤖 Multi-Bot Demo</h1>
        <p>Демонстрация на 5 различни чатбота за различни бизнес нужди</p>
    </div>
    
    <div class="bots-grid">
        <div class="bot-card" onclick="openBot('tourism_bot')">
            <div class="bot-icon">🏛️</div>
            <div class="bot-name">TourismBot</div>
            <div class="bot-description">Туристически съвети за България - забележителности, хотели, транспорт</div>
            <div class="bot-port">Порт: 5001</div>
            <button class="bot-button">Отвори TourismBot</button>
        </div>
        
        <div class="bot-card" onclick="openBot('tech_support_bot')">
            <div class="bot-icon">🔧</div>
            <div class="bot-name">TechSupportBot</div>
            <div class="bot-description">Техническа поддръжка - инсталация, проблеми, функции</div>
            <div class="bot-port">Порт: 5002</div>
            <button class="bot-button">Отвори TechSupportBot</button>
        </div>
        
        <div class="bot-card" onclick="openBot('sales_bot')">
            <div class="bot-icon">💰</div>
            <div class="bot-name">SalesBot</div>
            <div class="bot-description">Продажби и консултации - продукти, цени, демо</div>
            <div class="bot-port">Порт: 5003</div>
            <button class="bot-button">Отвори SalesBot</button>
        </div>
        
        <div class="bot-card" onclick="openBot('hr_bot')">
            <div class="bot-icon">👥</div>
            <div class="bot-name">HRBot</div>
            <div class="bot-description">HR помощник - позиции, бенефити, кандидатиране</div>
            <div class="bot-port">Порт: 5004</div>
            <button class="bot-button">Отвори HRBot</button>
        </div>
        
        <div class="bot-card" onclick="openBot('customer_service_bot')">
            <div class="bot-icon">🎧</div>
            <div class="bot-name">CustomerServiceBot</div>
            <div class="bot-description">Клиентски сервиз - поръчки, рекламации, помощ</div>
            <div class="bot-port">Порт: 5005</div>
            <button class="bot-button">Отвори CustomerServiceBot</button>
        </div>
    </div>
    
    <div class="footer">
        <p>© 2025 Multi-Bot Demo - Демонстрация на Rasa чатботове</p>
    </div>

    <script>
        function openBot(botName) {
            const botUrls = {
                'tourism_bot': 'bots/tourism_bot/web/index.html',
                'tech_support_bot': 'bots/tech_support_bot/web/index.html',
                'sales_bot': 'bots/sales_bot/web/index.html',
                'hr_bot': 'bots/hr_bot/web/index.html',
                'customer_service_bot': 'bots/customer_service_bot/web/index.html'
            };
            
            window.open(botUrls[botName], '_blank');
        }
    </script>
</body>
</html>
"""
    
    with open("dashboard.html", 'w', encoding='utf-8') as f:
        f.write(dashboard_content)

if __name__ == "__main__":
    create_bot_structure()

