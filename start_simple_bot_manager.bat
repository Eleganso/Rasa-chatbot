@echo off
echo ========================================
echo    🤖 ПРОСТ МУЛТИ-БОТ МЕНИДЖЪР
echo ========================================
echo.

cd /d "%~dp0"

echo 🔧 Активиране на Python среда...
call rasa_env\Scripts\activate.bat

echo.
echo 🚀 Стартиране на Simple Multi-Bot Manager...
echo.

python simple_bot_manager.py

pause
