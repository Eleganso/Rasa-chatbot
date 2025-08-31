@echo off
echo ========================================
echo    МУЛТИ-БОТ СИСТЕМА - ТЕСТОВЕ
echo ========================================
echo.
echo Стартиране на PowerShell тестове...
echo.

powershell -ExecutionPolicy Bypass -File "test_bots.ps1"

echo.
pause
