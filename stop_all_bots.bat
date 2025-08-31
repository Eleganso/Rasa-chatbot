@echo off
echo ========================================
echo    СПИРАНЕ НА ВСИЧКИ БОТОВЕ
echo ========================================
echo.
echo Спиране на всички Docker контейнери...
echo.

docker stop $(docker ps -q)

echo.
echo Всички ботове са спрени.
echo.
pause
