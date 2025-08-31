@echo off
echo ========================================
echo    Ресторант 'Златна вилица' - Трениране
echo ========================================
echo.
cd /d "%~dp0"
echo 📚 Трениране на Ресторант 'Златна вилица'...
echo.
cd bots\zlatna_vilitsa_restaurant\rasa
echo 📁 Създаване на models директория...
if not exist models mkdir models
echo.
echo 🔧 Трениране с Docker...
docker run --rm -v "%cd%:/app" rasa/rasa:3.6.21 train --force
if %errorlevel% neq 0 (
    echo ❌ Грешка при трениране!
    echo.
    echo 💡 Уверете се, че Docker Desktop е стартиран!
    pause
    exit /b 1
)
echo.
echo ✅ Тренирането завършено успешно!
echo 📦 Моделът е създаден в models/ директорията
echo.
pause
