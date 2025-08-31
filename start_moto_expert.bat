@echo off
echo ========================================
echo    АВТОСЕРВИЗ "МОТО ЕКСПЕРТ" БОТ
echo ========================================
echo.
echo Стартиране на Автосервиз "Мото Експерт" бот...
echo Порт: 5010
echo API: http://localhost:5010/webhooks/rest/webhook
echo Web интерфейс: http://localhost:5010
echo.
echo Изчакайте 15-20 секунди за зареждане...
echo.

REM Стартиране на бота в background
start /B docker run -v %cd%/bots/moto_expert_autoservice/rasa:/app -p 5010:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005

REM Изчакване за зареждане
timeout /t 20 /nobreak >nul

REM Отваряне на web интерфейса
start http://localhost:5010

echo.
echo Ботът е стартиран и web интерфейсът е отворен!
echo Натиснете Ctrl+C за да спрете бота.
echo.

REM Изчакване за спиране
docker run -v %cd%/bots/moto_expert_autoservice/rasa:/app -p 5010:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005

echo.
echo Ботът е спрян.
pause
