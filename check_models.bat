@echo off
echo =========================================
echo    SofiaBot Models Information
echo =========================================
echo.

echo Available models in rasa\models\:
echo.
dir rasa\models\*.tar.gz /b /o-d
echo.

echo Model Details:
echo ===============
echo.

echo 1. 20250828-153046-mad-quiver.tar.gz (LATEST)
echo    - Training Date: 2025-08-28 15:30:46
echo    - Features: SofiaBot personality + Bulgarian examples
echo    - Size: 26MB
echo    - Status: ✅ RECOMMENDED - Latest and best model
echo.

echo 2. 20250828-152359-hot-salamander.tar.gz
echo    - Training Date: 2025-08-28 15:23:59
echo    - Features: Basic improvements
echo    - Size: 26MB
echo    - Status: ⚠️  Outdated
echo.

echo 3. 20250828-152114-libretto-mason.tar.gz
echo    - Training Date: 2025-08-28 15:21:14
echo    - Features: Initial improvements
echo    - Size: 24MB
echo    - Status: ⚠️  Outdated
echo.

echo 4. 20250828-142409-sienna-specter.tar.gz
echo    - Training Date: 2025-08-28 14:24:09
echo    - Features: Original model
echo    - Size: 24MB
echo    - Status: ❌ Very outdated
echo.

echo =========================================
echo    Current Configuration
echo =========================================
echo.

echo Current start script uses:
if exist start_sofia_bot.bat (
    findstr "models/" start_sofia_bot.bat
) else (
    echo start_sofia_bot.bat not found
)

echo.
echo Recommended start script uses:
if exist start_sofia_bot_improved.bat (
    findstr "models/" start_sofia_bot_improved.bat
) else (
    echo start_sofia_bot_improved.bat not found
)

echo.
echo =========================================
echo    Recommendations
echo =========================================
echo.
echo ✅ Use: start_sofia_bot_improved.bat
echo ❌ Avoid: start_sofia_bot.bat (uses old model)
echo.
echo The improved script will show you exactly which model is being used!
echo.
pause

