@echo off
echo =========================================
echo    Starting DragonForgedDreams Bot V2
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Starting DragonForgedDreams Bot V2 server...
echo Starting DragonForgedDreams Bot V2 server on port 6002...
start "DragonForgedDreams Bot V2 Server" cmd /k "docker run --rm -v "%cd%\bots\dragonforged_bot_v2\rasa:/app" -p 6002:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005"

echo.
echo Waiting for DragonForgedDreams Bot V2 to start...
timeout /t 15 /nobreak >nul

echo.
echo Step 3: Opening DragonForgedDreams Bot V2 chat interface...
start "" "bots\dragonforged_bot_v2\web\index.html"

echo.
echo =========================================
echo    DragonForgedDreams Bot V2 Ready!
echo =========================================
echo.
echo ✅ DragonForgedDreams Bot V2 server is running on http://localhost:6002
echo ✅ DragonForgedDreams Bot V2 chat interface opened in your browser
echo ✅ Detailed service and pricing bot
echo.
echo Chat interface location:
echo   bots\dragonforged_bot_v2\web\index.html
echo.
echo Enjoy testing DragonForgedDreams Bot V2! 🎉
echo.
pause

