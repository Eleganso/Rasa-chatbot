@echo off
title МУЛТИ-БОТ СИСТЕМА - МЕНЮ
color 0A

:menu
cls
echo ========================================
echo    МУЛТИ-БОТ СИСТЕМА - МЕНЮ
echo ========================================
echo.
echo Изберете опция:
echo.
echo [1] DragonForgedDreams V2 (Порт 5005)
echo [2] Салон "Златна коса" (Порт 5006)
echo [3] Ресторант "Златна вилица" (Порт 5007)
echo [4] Хотел "Гранд София" (Порт 5008)
echo [5] Медицински център "Здраве+" (Порт 5009)
echo [6] Автосервиз "Мото Експерт" (Порт 5010)
echo.
echo [S] Статус на ботовете
echo [X] Спиране на всички ботове
echo [Q] Изход
echo.
echo ========================================
set /p choice="Въведете избор: "

if "%choice%"=="1" goto dragonforged
if "%choice%"=="2" goto zlatna_kosa
if "%choice%"=="3" goto zlatna_vilitsa
if "%choice%"=="4" goto grand_sofia
if "%choice%"=="5" goto zdrave_medical
if "%choice%"=="6" goto moto_expert
if "%choice%"=="S" goto status
if "%choice%"=="s" goto status
if "%choice%"=="X" goto stop_all
if "%choice%"=="x" goto stop_all
if "%choice%"=="Q" goto exit
if "%choice%"=="q" goto exit

echo Невалиден избор!
timeout /t 2 >nul
goto menu

:dragonforged
cls
echo Стартиране на DragonForgedDreams V2...
call start_dragonforged_v2.bat
goto menu

:zlatna_kosa
cls
echo Стартиране на Салон "Златна коса"...
call start_zlatna_kosa.bat
goto menu

:zlatna_vilitsa
cls
echo Стартиране на Ресторант "Златна вилица"...
call start_zlatna_vilitsa.bat
goto menu

:grand_sofia
cls
echo Стартиране на Хотел "Гранд София"...
call start_grand_sofia.bat
goto menu

:zdrave_medical
cls
echo Стартиране на Медицински център "Здраве+"...
call start_zdrave_medical.bat
goto menu

:moto_expert
cls
echo Стартиране на Автосервиз "Мото Експерт"...
call start_moto_expert.bat
goto menu

:status
cls
call check_bots_status.bat
goto menu

:stop_all
cls
echo Спиране на всички ботове...
call stop_all_bots.bat
goto menu

:exit
cls
echo Благодаря за използването на мулти-бот системата!
echo.
pause
exit
