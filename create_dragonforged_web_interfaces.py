#!/usr/bin/env python3
"""
Create web interfaces for DragonForgedDreams bots
"""

import os

def create_web_interface(bot_name, port, title, description):
    """Create web interface for a bot"""
    
    web_dir = f"bots/{bot_name}/web"
    os.makedirs(web_dir, exist_ok=True)
    
    html_content = f"""<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
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
        <h1>🤖 {title}</h1>
        <p>{description}</p>
    </div>
    
    <div class="chat-container">
        <div class="chat-header">
            💬 Чат с {title}
        </div>
        
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <div class="message-content">
                    Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?
                </div>
            </div>
        </div>
        
        <div class="typing-indicator" id="typingIndicator">
            {title} пише...
        </div>
        
        <div class="chat-input">
            <input type="text" id="messageInput" placeholder="Напишете вашето съобщение..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Изпрати</button>
        </div>
    </div>

    <script>
        const API_URL = 'http://localhost:{port}/webhooks/rest/webhook';
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

def main():
    """Create web interfaces for both bots"""
    
    # Create V1 interface
    create_web_interface(
        "dragonforged_bot_v1",
        6001,
        "DragonForgedDreams Bot V1",
        "Професионални бизнес решения - чатботове, сайтове, SEO"
    )
    
    # Create V2 interface
    create_web_interface(
        "dragonforged_bot_v2",
        6002,
        "DragonForgedDreams Bot V2",
        "Детайлни услуги и цени - QR меню, PWA, Telegram ботове"
    )
    
    print("✅ Web interfaces created for both DragonForgedDreams bots!")

if __name__ == "__main__":
    main()

