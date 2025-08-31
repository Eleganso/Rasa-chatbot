# 🐉 DragonForgedDreams Bot V2 - Website Integration Guide

## Overview

This guide explains how to integrate DragonForgedDreams Bot V2 into your existing website at dragonforgeddreams.com.

## Integration Options

### Option 1: Chat Widget (Recommended)

Add a floating chat widget to your website that connects to the bot API.

#### HTML Implementation

```html
<!DOCTYPE html>
<html lang="bg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DragonForgedDreams - Professional Digital Solutions</title>
    <style>
        /* Chat Widget Styles */
        .chat-widget {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            height: 500px;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            z-index: 1000;
            display: none;
            flex-direction: column;
            overflow: hidden;
        }
        
        .chat-widget.active {
            display: flex;
        }
        
        .chat-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            text-align: center;
            font-weight: bold;
        }
        
        .chat-messages {
            flex: 1;
            padding: 15px;
            overflow-y: auto;
            max-height: 350px;
        }
        
        .message {
            margin-bottom: 10px;
            display: flex;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message.bot {
            justify-content: flex-start;
        }
        
        .message-content {
            max-width: 80%;
            padding: 10px 15px;
            border-radius: 15px;
            word-wrap: break-word;
        }
        
        .message.user .message-content {
            background: #007bff;
            color: white;
        }
        
        .message.bot .message-content {
            background: #f8f9fa;
            color: #333;
            border: 1px solid #e0e0e0;
        }
        
        .chat-input {
            padding: 15px;
            border-top: 1px solid #e0e0e0;
            display: flex;
        }
        
        .chat-input input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 20px;
            margin-right: 10px;
        }
        
        .chat-input button {
            padding: 10px 20px;
            background: #007bff;
            color: white;
            border: none;
            border-radius: 20px;
            cursor: pointer;
        }
        
        .chat-toggle {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 50%;
            color: white;
            border: none;
            font-size: 24px;
            cursor: pointer;
            z-index: 1001;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        
        .typing-indicator {
            padding: 10px;
            color: #666;
            font-style: italic;
            display: none;
        }
    </style>
</head>
<body>
    <!-- Your existing website content here -->
    
    <!-- Chat Toggle Button -->
    <button class="chat-toggle" onclick="toggleChat()">💬</button>
    
    <!-- Chat Widget -->
    <div class="chat-widget" id="chatWidget">
        <div class="chat-header">
            🐉 DragonForgedDreams Assistant
        </div>
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">
                <div class="message-content">
                    Здравейте! Добре дошли в DragonForged Dreams! Как мога да ви помогна днес?
                </div>
            </div>
        </div>
        <div class="typing-indicator" id="typingIndicator">
            DragonForgedDreams Assistant пише...
        </div>
        <div class="chat-input">
            <input type="text" id="messageInput" placeholder="Напишете вашето съобщение..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Изпрати</button>
        </div>
    </div>

    <script>
        const BOT_API = 'https://dragonforgeddreams.com/webhooks/rest/webhook';
        let chatOpen = false;
        
        function toggleChat() {
            const widget = document.getElementById('chatWidget');
            chatOpen = !chatOpen;
            
            if (chatOpen) {
                widget.classList.add('active');
            } else {
                widget.classList.remove('active');
            }
        }
        
        function addMessage(content, isUser = false) {
            const messagesDiv = document.getElementById('chatMessages');
            const messageDiv = document.createElement('div');
            messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
            
            const contentDiv = document.createElement('div');
            contentDiv.className = 'message-content';
            contentDiv.textContent = content;
            
            messageDiv.appendChild(contentDiv);
            messagesDiv.appendChild(messageDiv);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }
        
        function showTyping() {
            document.getElementById('typingIndicator').style.display = 'block';
        }
        
        function hideTyping() {
            document.getElementById('typingIndicator').style.display = 'none';
        }
        
        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            
            if (!message) return;
            
            // Add user message
            addMessage(message, true);
            input.value = '';
            
            // Show typing indicator
            showTyping();
            
            try {
                const response = await fetch(BOT_API, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        message: message,
                        sender: 'website_user_' + Date.now()
                    })
                });
                
                const data = await response.json();
                hideTyping();
                
                if (data && data.length > 0) {
                    data.forEach(item => {
                        if (item.text) {
                            addMessage(item.text);
                        }
                    });
                } else {
                    addMessage('Извинявам се, имам проблем с обработката на вашето съобщение. Моля, опитайте отново.');
                }
            } catch (error) {
                hideTyping();
                addMessage('Извинявам се, има технически проблем. Моля, свържете се с нас директно.');
                console.error('Bot API Error:', error);
            }
        }
        
        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }
        
        // Auto-open chat on page load (optional)
        // setTimeout(() => toggleChat(), 3000);
    </script>
</body>
</html>
```

### Option 2: Iframe Integration

Embed the bot as an iframe in a specific section of your website.

```html
<!-- Add this to any page where you want the bot -->
<div class="bot-section">
    <h2>💬 Говорете с нашия асистент</h2>
    <p>Получете бързи отговори на въпросите ви за нашите услуги</p>
    
    <iframe 
        src="https://dragonforgeddreams.com" 
        width="100%" 
        height="600" 
        style="border: none; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2);"
        title="DragonForgedDreams Chat Assistant">
    </iframe>
</div>
```

### Option 3: API Integration

Use the bot API directly in your custom chat implementation.

```javascript
// Example API usage
async function askBot(question) {
    try {
        const response = await fetch('https://dragonforgeddreams.com/webhooks/rest/webhook', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: question,
                sender: 'custom_user'
            })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Bot API Error:', error);
        return null;
    }
}

// Usage example
askBot('Какви са цените за QR меню?').then(response => {
    if (response && response.length > 0) {
        console.log('Bot response:', response[0].text);
    }
});
```

## Bot Capabilities

DragonForgedDreams Bot V2 can handle the following topics:

### 🍽️ QR Menu Services
- **Starter Package**: 4.99 BGN/month
- **Professional Package**: 19.99 BGN/month  
- **Signature Package**: 39.99 BGN/month

### 🤖 Chatbot Development
- Website chatbots
- Social media automation
- 24/7 customer support
- Lead generation

### 📱 Telegram Bots
- Business process automation
- System integrations
- Custom workflows

### 🌐 Website Development
- Modern, responsive websites
- SEO optimization
- E-commerce solutions
- Starting from 400 BGN

### 📱 PWA Applications
- Progressive Web Apps
- Mobile-like experience
- Offline functionality

### 🔍 SEO Services
- Google ranking optimization
- Technical SEO
- Content strategy
- Link building

### 🛠️ Technical Support
- Professional support: 50 BGN/month
- Problem resolution
- Updates and maintenance

### 💬 Free Consultation
- Personalized recommendations
- Strategy planning
- Service selection help

## Customization Options

### 1. Styling Customization

Modify the CSS in the chat widget to match your website's design:

```css
/* Custom colors for your brand */
.chat-header {
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
}

.chat-toggle {
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
}
```

### 2. Welcome Message

Customize the initial greeting message:

```javascript
// Change the welcome message
const welcomeMessage = "Здравейте! Добре дошли в [Your Company Name]! Как мога да ви помогна?";
```

### 3. Auto-Open Triggers

Set when the chat should automatically open:

```javascript
// Open chat after 30 seconds
setTimeout(() => toggleChat(), 30000);

// Open chat when user scrolls to bottom
window.addEventListener('scroll', () => {
    if ((window.innerHeight + window.scrollY) >= document.body.offsetHeight) {
        toggleChat();
    }
});
```

## Testing the Integration

### 1. Test Questions

Try these questions to test the bot:

- "Здравейте"
- "Какви услуги предлагате?"
- "Колко струва QR меню?"
- "Искам чатбот за сайта ми"
- "Имате ли безплатна консултация?"
- "Как да се свържа с вас?"

### 2. Expected Responses

The bot should provide:
- Professional greetings
- Service descriptions
- Specific pricing information
- Contact details
- Free consultation offers

## Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check if the VPS is running
   - Verify the API endpoint is correct
   - Check browser console for errors

2. **CORS errors**
   - Ensure the bot server has CORS enabled
   - Check nginx configuration

3. **SSL certificate issues**
   - Verify SSL certificate is valid
   - Check domain configuration

### Debug Commands

```bash
# Check bot status
curl https://dragonforgeddreams.com/status

# Test bot API
curl -X POST https://dragonforgeddreams.com/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"message": "здравейте", "sender": "test"}'
```

## Support

For technical support with the integration:
- Email: info@dragonforgeddreams.com
- Website: https://dragonforgeddreams.com
- Bot API: https://dragonforgeddreams.com/webhooks/rest/webhook

---

*DragonForgedDreams Bot V2 - Professional chatbot integration for dragonforgeddreams.com*

