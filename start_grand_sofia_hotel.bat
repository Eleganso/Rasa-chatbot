@echo off
echo ========================================
echo    Хотел "Гранд София" - Чатбот
echo ========================================
echo.
cd /d "%~dp0"
echo 🏨 Стартиране на хотел "Гранд София" чатбот...
echo.
cd bots\grand_sofia_hotel\rasa
echo 📚 Трениране на модела...
docker run --rm -v "%cd%:/app" rasa/rasa:3.6.21 train --force
if %errorlevel% neq 0 (
    echo ❌ Грешка при тренирането на модела!
    pause
    exit /b 1
)
echo ✅ Моделът е трениран успешно!
echo.
echo 🤖 Стартиране на Rasa сървъра...
echo 📍 API: http://localhost:5009
echo 🌐 Уеб интерфейс: http://localhost:5009/webhooks/rest/webhook
echo.
docker run --rm -v "%cd%:/app" -p 5009:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005
pause
