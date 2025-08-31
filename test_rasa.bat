@echo off
echo =========================================
echo    Testing Rasa API
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Checking if Rasa server is running...
powershell -Command "try { Invoke-RestMethod -Uri 'http://localhost:5005/status' -Method GET; Write-Host 'Rasa server is running!' } catch { Write-Host 'Starting Rasa server...' }"

if %errorlevel% neq 0 (
    echo Starting Rasa server...
    start "Rasa Server" cmd /k "docker run --rm -v "%cd%\rasa:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005 --model models/20250828-142409-sienna-specter.tar.gz"
    echo Waiting for server to start...
    timeout /t 20 /nobreak >nul
)

echo.
echo Step 3: Testing Rasa API with sample message...
powershell -Command "try { $response = Invoke-RestMethod -Uri 'http://localhost:5005/webhooks/rest/webhook' -Method POST -ContentType 'application/json' -Body '{\"sender\": \"test_user\", \"message\": \"Hello\"}'; Write-Host 'Response:' $response } catch { Write-Host 'Error:' $_.Exception.Message }"

echo.
echo Step 4: Testing intent classification...
powershell -Command "try { $response = Invoke-RestMethod -Uri 'http://localhost:5005/model/parse' -Method POST -ContentType 'application/json' -Body '{\"text\": \"Hello\"}'; Write-Host 'Intent:' $response.intent.name } catch { Write-Host 'Error:' $_.Exception.Message }"

echo.
echo Step 5: Testing with Bulgarian message...
powershell -Command "try { $response = Invoke-RestMethod -Uri 'http://localhost:5005/webhooks/rest/webhook' -Method POST -ContentType 'application/json' -Body '{\"sender\": \"test_user\", \"message\": \"Здравей\"}'; Write-Host 'Response:' $response } catch { Write-Host 'Error:' $_.Exception.Message }"

echo.
echo Step 6: Testing with weather query...
powershell -Command "try { $response = Invoke-RestMethod -Uri 'http://localhost:5005/webhooks/rest/webhook' -Method POST -ContentType 'application/json' -Body '{\"sender\": \"test_user\", \"message\": \"What is the weather like?\"}'; Write-Host 'Response:' $response } catch { Write-Host 'Error:' $_.Exception.Message }"

echo.
echo =========================================
echo    API Test Complete!
echo =========================================
echo.
echo To test more messages manually:
echo 1. Open browser and go to: http://localhost:5005
echo 2. Or use PowerShell:
echo    Invoke-RestMethod -Uri "http://localhost:5005/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body '{"sender": "user", "message": "Your message here"}'
echo.
pause
