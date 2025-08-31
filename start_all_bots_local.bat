@echo off
echo ========================================
echo    СТАРТИРАНЕ НА ВСИЧКИ БОТОВЕ ЛОКАЛНО
echo ========================================
echo.
echo Стартиране на всички 6 бота с Docker Compose...
echo.
echo Портове:
echo - DragonForgedDreams V2: 5005
echo - Салон "Златна коса": 5006
echo - Ресторант "Златна вилица": 5007
echo - Хотел "Гранд София": 5008
echo - Медицински център "Здраве+": 5009
echo - Автосервиз "Мото Експерт": 5010
echo - Nginx (Web интерфейси): 8080
echo.
echo Изчакайте 30-60 секунди за зареждане на всички ботове...
echo.

REM Спиране на съществуващи контейнери
docker-compose -f docker-compose-local.yml down

REM Стартиране на всички ботове
docker-compose -f docker-compose-local.yml up -d

REM Изчакване за зареждане
timeout /t 45 /nobreak >nul

REM Отваряне на главната страница
start http://localhost:8080

echo.
echo ========================================
echo    ВСИЧКИ БОТОВЕ СА СТАРТИРАНИ!
echo ========================================
echo.
echo 🌐 Web интерфейси:
echo - Главна страница: http://localhost:8080
echo - DragonForgedDreams V2: http://localhost:5005
echo - Салон "Златна коса": http://localhost:5006
echo - Ресторант "Златна вилица": http://localhost:5007
echo - Хотел "Гранд София": http://localhost:5008
echo - Медицински център "Здраве+": http://localhost:5009
echo - Автосервиз "Мото Експерт": http://localhost:5010
echo.
echo 🔧 API Endpoints:
echo - DragonForgedDreams V2: http://localhost:5005/webhooks/rest/webhook
echo - Салон "Златна коса": http://localhost:5006/webhooks/rest/webhook
echo - Ресторант "Златна вилица": http://localhost:5007/webhooks/rest/webhook
echo - Хотел "Гранд София": http://localhost:5008/webhooks/rest/webhook
echo - Медицински център "Здраве+": http://localhost:5009/webhooks/rest/webhook
echo - Автосервиз "Мото Експерт": http://localhost:5010/webhooks/rest/webhook
echo.
echo Натиснете Enter за да спрете всички ботове...
pause

REM Спиране на всички ботове
docker-compose -f docker-compose-local.yml down

echo.
echo Всички ботове са спрени.
pause
