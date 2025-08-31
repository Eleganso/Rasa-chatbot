@echo off
echo =========================================
echo    Creating DragonForgedDreams Bots
echo =========================================
echo.

echo Step 1: Creating DragonForgedDreams Bot V1...
python create_dragonforged_bot_v1.py

echo.
echo Step 2: Creating DragonForgedDreams Bot V2...
python create_dragonforged_bot_v2.py

echo.
echo Step 3: Training both bots...
echo.

echo Training DragonForgedDreams Bot V1...
docker run --rm -v "%cd%\bots\dragonforged_bot_v1\rasa:/app" rasa/rasa:3.6.21 train --force

echo.
echo Training DragonForgedDreams Bot V2...
docker run --rm -v "%cd%\bots\dragonforged_bot_v2\rasa:/app" rasa/rasa:3.6.21 train --force

echo.
echo =========================================
echo    DragonForgedDreams Bots Ready! 🎉
echo =========================================
echo.
echo ✅ DragonForgedDreams Bot V1 (Port 6001)
echo    - 8 intents (services, prices, chatbots, websites, etc.)
echo    - Professional responses
echo    - Focus on business solutions
echo.
echo ✅ DragonForgedDreams Bot V2 (Port 6002)
echo    - 13 intents (QR menu, SEO, PWA, Telegram bots, etc.)
echo    - Detailed pricing information
echo    - More specific service focus
echo.
echo 🚀 To start the bots:
echo    - V1: .\start_dragonforged_v1.bat
echo    - V2: .\start_dragonforged_v2.bat
echo.
pause

