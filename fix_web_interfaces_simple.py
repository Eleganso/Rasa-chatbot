#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Web Interfaces Simple
Опростено поправяне на уеб интерфейсите
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_bot_html(bot_name, bot_description, welcome_message):
    """Създава HTML за бота"""
    return f"""<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{bot_name}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        
        .chat-container {{
            width: 90%;
            max-width: 800px;
            height: 80vh;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            text-align: center;
            position: relative;
        }}
        
        .header h1 {{
            font-size: 24px;
            margin-bottom: 5px;
        }}
        
        .header p {{
            font-size: 14px;
            opacity: 0.9;
        }}
        
        .chat-status {{
            background: #4CAF50;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 14px;
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
            align-items: flex-start;
        }}
        
        .message.bot {{
            justify-content: flex-start;
        }}
        
        .message.user {{
            justify-content: flex-end;
        }}
        
        .message-content {{
            max-width: 70%;
            padding: 12px 16px;
            border-radius: 18px;
            word-wrap: break-word;
        }}
        
        .message.bot .message-content {{
            background: #e3f2fd;
            color: #1565c0;
        }}
        
        .message.user .message-content {{
            background: #667eea;
            color: white;
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
            border-color: #667eea;
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
        
        .quick-replies {{
            display: flex;
            gap: 10px;
            margin-top: 10px;
            flex-wrap: wrap;
        }}
        
        .quick-reply {{
            padding: 8px 16px;
            background: #e3f2fd;
            color: #1565c0;
            border: none;
            border-radius: 15px;
            cursor: pointer;
            font-size: 14px;
            transition: background 0.3s;
        }}
        
        .quick-reply:hover {{
            background: #bbdefb;
        }}
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="header">
            <h1>{bot_name}</h1>
            <p>{bot_description}</p>
        </div>
        
        <div class="chat-status">
            Чат с {bot_name}
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <div class="message-content">
                    {welcome_message}
                </div>
            </div>
        </div>
        
        <div class="chat-input">
            <input type="text" id="messageInput" placeholder="Напишете вашето съобщение..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Изпрати</button>
        </div>
        
        <div class="quick-replies" id="quickReplies">
            <button class="quick-reply" onclick="sendQuickReply('здравей')">здравей</button>
            <button class="quick-reply" onclick="sendQuickReply('цени')">цени</button>
            <button class="quick-reply" onclick="sendQuickReply('информация')">информация</button>
        </div>
    </div>

    <script>
        const API_URL = window.location.origin + '/webhooks/rest/webhook';
        const chatMessages = document.getElementById('chatMessages');
        const messageInput = document.getElementById('messageInput');
        
        function addMessage(content, isUser = false) {{
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${{isUser ? 'user' : 'bot'}}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            chatMessages.appendChild(messageDiv);
            
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }}
        
        function sendMessage() {{
            const message = messageInput.value.trim();
            if (!message) return;
            
            addMessage(message, true);
            messageInput.value = '';
            
            fetch(API_URL, {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                }},
                body: JSON.stringify({{
                    message: message
                }})
            }})
            .then(response => response.json())
            .then(data => {{
                if (data && data.length > 0) {{
                    data.forEach(response => {{
                        if (response.text) {{
                            addMessage(response.text);
                        }}
                    }});
                }}
            }})
            .catch(error => {{
                console.error('Error:', error);
                addMessage('Съжалявам, има проблем с връзката. Моля, опитайте отново.');
            }});
        }}
        
        function sendQuickReply(text) {{
            messageInput.value = text;
            sendMessage();
        }}
        
        function handleKeyPress(event) {{
            if (event.key === 'Enter') {{
                sendMessage();
            }}
        }}
        
        // Auto-scroll to bottom when window gains focus
        window.addEventListener('focus', () => {{
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }});
        
        // Auto-scroll when tab becomes visible
        document.addEventListener('visibilitychange', () => {{
            if (!document.hidden) {{
                chatMessages.scrollTop = chatMessages.scrollHeight;
            }}
        }});
    </script>
</body>
</html>"""

def fix_web_interfaces_simple():
    """Поправя уеб интерфейсите на ботовете"""
    print("🔧 ПОПРАВЯНЕ НА УЕБ ИНТЕРФЕЙСИТЕ")
    print("="*50)
    
    config = load_config()
    host = "37.60.225.86"
    username = input("Потребителско име (root): ").strip() or "root"
    password = input("Парола: ").strip()
    
    try:
        # Свързване с VPS
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        print("✅ Успешно свързване!")
        
        # Спиране на контейнерите
        print("\n🛑 Спиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose down")
        time.sleep(5)
        
        # Поправяне на уеб интерфейсите
        print("\n🔧 Поправяне на уеб интерфейсите...")
        
        bot_configs = {
            'zlatna_kosa': {
                'name': 'Салон "Златна коса"',
                'description': 'Професионални козметични услуги',
                'welcome': 'Привет! ✨ Добре дошли в салон "Златна коса"! Как мога да ви помогна днес?'
            },
            'zlatna_vilitsa': {
                'name': 'Ресторант "Златна вилица"',
                'description': 'Традиционна българска кухня',
                'welcome': 'Добре дошли в ресторант "Златна вилица"! 🍽️ Как мога да ви помогна днес?'
            },
            'grand_sofia': {
                'name': 'Хотел "Гранд София"',
                'description': 'Луксозно настаняване в центъра на София',
                'welcome': 'Добре дошли в хотел "Гранд София"! 🏨 Как мога да ви помогна днес?'
            },
            'zdrave_medical': {
                'name': 'Медицински център "Здраве+"',
                'description': 'Професионална медицинска грижа',
                'welcome': 'Здравейте! 👋 Аз съм д-р Мария, ваш виртуален асистент. Как мога да ви помогна?'
            },
            'moto_expert': {
                'name': 'Автосервиз "Мото Експерт"',
                'description': 'Професионални автомобилни услуги',
                'welcome': 'Здравейте! 👋 Аз съм вашият виртуален автосервиз асистент. Как мога да ви помогна?'
            }
        }
        
        for bot_id, bot_config in bot_configs.items():
            print(f"\n🤖 Поправяне на {bot_config['name']}...")
            
            # Създаване на нов HTML
            html_content = create_bot_html(
                bot_config['name'],
                bot_config['description'],
                bot_config['welcome']
            )
            
            # Записване на новия файл
            remote_web_dir = f"/root/multi-bots/bots/{bot_id}/web"
            ssh.exec_command(f"echo '{html_content.replace(chr(39), chr(39) + chr(34) + chr(39) + chr(34) + chr(39))}' > {remote_web_dir}/index.html")
            
            print(f"   ✅ {bot_config['name']} - поправен")
        
        # Стартиране на контейнерите отново
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        print(f"\n🎉 Поправянето завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for bot_id, bot_config in bot_configs.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    fix_web_interfaces_simple()
