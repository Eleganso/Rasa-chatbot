@echo off
echo ========================================
echo    Медицински център "Здраве+" - Чатбот
echo ========================================
echo.
cd /d "%~dp0"
echo 🏥 Стартиране на медицински център "Здраве+" чатбот...
echo.
cd bots\zdrave_medical_center\rasa
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
echo 📍 API: http://localhost:5010
echo 🌐 Уеб интерфейс: http://localhost:5010/webhooks/rest/webhook
echo.
docker run --rm -v "%cd%:/app" -p 5010:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005
pause
