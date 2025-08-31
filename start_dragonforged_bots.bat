@echo off
echo =========================================
echo    Starting DragonForgedDreams Bots
echo =========================================
echo.
echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin
echo.
echo Step 2: Starting both DragonForgedDreams bots...
echo.
echo Starting DragonForgedDreams Bot V1 (Port 6001)...
start "DragonForgedDreams Bot V1 Server" cmd /k "docker run --rm -v "%cd%\bots\dragonforged_bot_v1\rasa:/app" -p 6001:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005"
echo.
echo Starting DragonForgedDreams Bot V2 (Port 6002)...
start "DragonForgedDreams Bot V2 Server" cmd /k "docker run --rm -v "%cd%\bots\dragonforged_bot_v2\rasa:/app" -p 6002:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005"
echo.
echo Waiting for both bots to start...
timeout /t 30 /nobreak >nul
echo.
echo Step 3: Opening DragonForgedDreams Dashboard...
start "" "dragonforged_dashboard.html"
echo.
echo =========================================
echo    DragonForgedDreams Bots Ready! 🐉
echo =========================================
echo.
echo ✅ DragonForgedDreams Bot V1 (Port 6001)
echo    - 8 intents (services, prices, chatbots, websites, etc.)
echo    - Professional business approach
echo    - General services focus
echo.
echo ✅ DragonForgedDreams Bot V2 (Port 6002)
echo    - 13 intents (QR menu, SEO, PWA, Telegram bots, etc.)
echo    - Detailed pricing information
echo    - Specific services focus
echo.
echo 🌐 Dashboard opened in browser
echo    - Click on any bot card to open its chat interface
echo    - Compare the two different approaches
echo.
echo 🛑 To stop the bots:
echo    - Close the "DragonForgedDreams Bot V1 Server" window
echo    - Close the "DragonForgedDreams Bot V2 Server" window
echo.
pause

