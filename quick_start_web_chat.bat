@echo off
echo =========================================
echo    Quick Start - Web Chat Interface
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Checking Docker installation...
docker --version
if %errorlevel% neq 0 (
    echo Docker is not installed or not running!
    echo Please install Docker Desktop and start it
    pause
    exit /b 1
)

echo.
echo Step 3: Creating web chat interface...
if not exist "web_chat" mkdir web_chat

echo.
echo Step 4: Creating HTML chat interface...
(
echo ^<!DOCTYPE html^>
echo ^<html lang="en"^>
echo ^<head^>
echo     ^<meta charset="UTF-8"^>
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo     ^<title^>Rasa Chat Bot^</title^>
echo     ^<style^>
echo         body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f0f2f5; }
echo         .chat-container { max-width: 600px; margin: 0 auto; background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
echo         .chat-header { background: #1877f2; color: white; padding: 20px; border-radius: 10px 10px 0 0; text-align: center; }
echo         .chat-messages { height: 400px; overflow-y: auto; padding: 20px; }
echo         .message { margin-bottom: 15px; display: flex; }
echo         .message.user { justify-content: flex-end; }
echo         .message.bot { justify-content: flex-start; }
echo         .message-content { max-width: 70%%; padding: 10px 15px; border-radius: 20px; }
echo         .user .message-content { background: #1877f2; color: white; }
echo         .bot .message-content { background: #e4e6eb; color: #050505; }
echo         .chat-input { padding: 20px; border-top: 1px solid #e4e6eb; display: flex; }
echo         .chat-input input { flex: 1; padding: 12px; border: 1px solid #e4e6eb; border-radius: 20px; margin-right: 10px; }
echo         .chat-input button { padding: 12px 20px; background: #1877f2; color: white; border: none; border-radius: 20px; cursor: pointer; }
echo         .chat-input button:hover { background: #166fe5; }
echo         .typing { color: #65676b; font-style: italic; }
echo     ^</style^>
echo ^</head^>
echo ^<body^>
echo     ^<div class="chat-container"^>
echo         ^<div class="chat-header"^>
echo             ^<h2^>🤖 Rasa Chat Bot^</h2^>
echo             ^<p^>Powered by AI - Ask me anything!^</p^>
echo         ^</div^>
echo         ^<div class="chat-messages" id="chatMessages"^>
echo             ^<div class="message bot"^>
echo                 ^<div class="message-content"^>
echo                     Hello! I'm your Rasa bot. How can I help you today?
echo                 ^</div^>
echo             ^</div^>
echo         ^</div^>
echo         ^<div class="chat-input"^>
echo             ^<input type="text" id="messageInput" placeholder="Type your message..." onkeypress="handleKeyPress(event)"^>
echo             ^<button onclick="sendMessage()"^>Send^</button^>
echo         ^</div^>
echo     ^</div^>
echo.
echo     ^<script^>
echo         const chatMessages = document.getElementById('chatMessages'^);
echo         const messageInput = document.getElementById('messageInput'^);
echo         const senderId = 'web_user_' + Math.random().toString(36^).substr(2, 9^);
echo.
echo         function addMessage(message, isUser = false^) {
echo             const messageDiv = document.createElement('div'^);
echo             messageDiv.className = `message ${isUser ? 'user' : 'bot'}`;
echo             messageDiv.innerHTML = `^<div class="message-content"^>${message}^</div^>`;
echo             chatMessages.appendChild(messageDiv^);
echo             chatMessages.scrollTop = chatMessages.scrollHeight;
echo         }
echo.
echo         function showTyping() {
echo             const typingDiv = document.createElement('div'^);
echo             typingDiv.className = 'message bot';
echo             typingDiv.id = 'typing';
echo             typingDiv.innerHTML = '^<div class="message-content typing"^>Bot is typing...^</div^>';
echo             chatMessages.appendChild(typingDiv^);
echo             chatMessages.scrollTop = chatMessages.scrollHeight;
echo         }
echo.
echo         function hideTyping() {
echo             const typingDiv = document.getElementById('typing'^);
echo             if (typingDiv^) {
echo                 typingDiv.remove();
echo             }
echo         }
echo.
echo         async function sendMessage() {
echo             const message = messageInput.value.trim();
echo             if (!message^) return;
echo.
echo             // Add user message
echo             addMessage(message, true^);
echo             messageInput.value = '';
echo.
echo             // Show typing indicator
echo             showTyping();
echo.
echo             try {
echo                 const response = await fetch('http://localhost:5005/webhooks/rest/webhook', {
echo                     method: 'POST',
echo                     headers: {
echo                         'Content-Type': 'application/json',
echo                     },
echo                     body: JSON.stringify({
echo                         sender: senderId,
echo                         message: message
echo                     }^)
echo                 }^);
echo.
echo                 const data = await response.json();
echo                 hideTyping();
echo.
echo                 if (data && data.length > 0^) {
echo                     data.forEach(reply => {
echo                         if (reply.text^) {
echo                             addMessage(reply.text^);
echo                         }
echo                     }^);
echo                 } else {
echo                     addMessage('Sorry, I didn\'t understand that. Could you rephrase?'^);
echo                 }
echo             } catch (error^) {
echo                 hideTyping();
echo                 addMessage('Sorry, there was an error connecting to the bot. Please try again.'^);
echo                 console.error('Error:', error^);
echo             }
echo         }
echo.
echo         function handleKeyPress(event^) {
echo             if (event.key === 'Enter'^) {
echo                 sendMessage();
echo             }
echo         }
echo.
echo         // Focus on input when page loads
echo         window.onload = function() {
echo             messageInput.focus();
echo         };
echo     ^</script^>
echo ^</body^>
echo ^</html^>
) > web_chat\index.html

echo.
echo Step 5: Creating start script...
(
echo @echo off
echo echo Starting Rasa server...
echo docker run --rm -v "%cd%\rasa:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005 --model models/20250828-142409-sienna-specter.tar.gz
) > web_chat\start_rasa.bat

echo.
echo Step 6: Creating test script...
(
echo @echo off
echo echo Testing Rasa API...
echo powershell -Command "try { $response = Invoke-RestMethod -Uri 'http://localhost:5005/webhooks/rest/webhook' -Method POST -ContentType 'application/json' -Body '{\"sender\": \"test_user\", \"message\": \"Hello\"}'; Write-Host 'Response:' $response } catch { Write-Host 'Error:' $_.Exception.Message }"
echo pause
) > web_chat\test_api.bat

echo.
echo Step 7: Starting Rasa server...
echo Starting Rasa server in background...
start "Rasa Server" cmd /k "docker run --rm -v "%cd%\rasa:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005 --model models/20250828-142409-sienna-specter.tar.gz"

echo.
echo Waiting for server to start...
timeout /t 15 /nobreak >nul

echo.
echo Step 8: Opening web chat interface...
start "" "web_chat\index.html"

echo.
echo =========================================
echo    Web Chat Interface Ready!
echo =========================================
echo.
echo ✅ Rasa server is running on http://localhost:5005
echo ✅ Web chat interface opened in your browser
echo ✅ You can now chat with your bot!
echo.
echo To test the API manually:
echo   web_chat\test_api.bat
echo.
echo To restart Rasa server:
echo   web_chat\start_rasa.bat
echo.
echo Chat interface location:
echo   web_chat\index.html
echo.
echo Enjoy testing your Rasa bot! 🎉
echo.
pause
