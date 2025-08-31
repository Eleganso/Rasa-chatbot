@echo off
echo ========================================
echo    Салон "Златна коса" - Чатбот
echo ========================================
echo.

cd /d "%~dp0"

echo 🎨 Стартиране на салон "Златна коса" чатбот...
echo.

cd bots\zlatna_kosa_salon\rasa

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
echo 📍 API: http://localhost:5005
echo 🌐 Уеб интерфейс: http://localhost:5005/webhooks/rest/webhook
echo.

docker run --rm -v "%cd%:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005

pause
