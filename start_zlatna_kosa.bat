@echo off
echo ========================================
echo    САЛОН "ЗЛАТНА КОСА" БОТ
echo ========================================
echo.
echo Стартиране на Салон "Златна коса" бот...
echo Порт: 5006
echo API: http://localhost:5006/webhooks/rest/webhook
echo Web интерфейс: http://localhost:5006
echo.
echo Изчакайте 15-20 секунди за зареждане...
echo.

REM Стартиране на бота в background
start /B docker run -v %cd%/bots/zlatna_kosa_salon/rasa:/app -p 5006:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005

REM Изчакване за зареждане
timeout /t 20 /nobreak >nul

REM Отваряне на web интерфейса
start http://localhost:5006

echo.
echo Ботът е стартиран и web интерфейсът е отворен!
echo Натиснете Ctrl+C за да спрете бота.
echo.

REM Изчакване за спиране
docker run -v %cd%/bots/zlatna_kosa_salon/rasa:/app -p 5006:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005

echo.
echo Ботът е спрян.
pause
