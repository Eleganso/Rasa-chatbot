@echo off
echo ========================================
echo    Медицински център 'Здраве+' - Трениране
echo ========================================
echo.
cd /d "%~dp0"
echo 📚 Трениране на Медицински център 'Здраве+'...
echo.
cd bots\zdrave_medical_center\rasa
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
