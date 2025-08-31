@echo off
echo ========================================
echo    🤖 МУЛТИ-БОТ МЕНИДЖЪР
echo ========================================
echo.

cd /d "%~dp0"

echo 🔧 Активиране на Python среда...
call rasa_env\Scripts\activate.bat

echo.
echo 🚀 Стартиране на Multi-Bot Manager...
echo.

python bot_manager.py

pause
