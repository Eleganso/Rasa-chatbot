@echo off
echo =========================================
echo    Rasa VPS Deployment Package
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Checking Docker installation...
docker --version
if %errorlevel% neq 0 (
    echo Docker is not installed or not running!
    echo Please install Docker Desktop and start it
    pause
    exit /b 1
)

echo.
echo Step 3: Creating deployment package...
if not exist "deployment" mkdir deployment
if not exist "deployment\rasa" mkdir deployment\rasa

echo.
echo Step 4: Copying Rasa files...
xcopy "rasa\*" "deployment\rasa\" /E /I /Y

echo.
echo Step 5: Creating Docker Compose file...
(
echo version: '3.8'
echo services:
echo   rasa:
echo     image: rasa/rasa:3.6.21
echo     ports:
echo       - "5005:5005"
echo     volumes:
echo       - ./rasa:/app
echo     command: run --enable-api --cors "*" --port 5005
echo     restart: unless-stopped
echo.
echo   actions:
echo     image: rasa/rasa-sdk:3.6.2
echo     ports:
echo       - "5055:5055"
echo     volumes:
echo       - ./rasa/actions:/app/actions
echo     command: run --enable-api --cors "*" --port 5055
echo     restart: unless-stopped
) > deployment\docker-compose.yml

echo.
echo Step 6: Creating deployment script...
(
echo #!/bin/bash
echo echo "Starting Rasa with Docker Compose..."
echo docker-compose up -d
echo echo "Rasa is running on http://localhost:5005"
echo echo "Actions server is running on http://localhost:5055"
) > deployment\deploy.sh

echo.
echo Step 7: Creating README file...
(
echo # Rasa VPS Deployment
echo.
echo ## Quick Start
echo.
echo 1. Upload the deployment folder to your VPS
echo 2. Install Docker and Docker Compose on your VPS
echo 3. Run: `docker-compose up -d`
echo 4. Access Rasa API at: `http://your-vps-ip:5005`
echo.
echo ## API Endpoints
echo - POST `/webhooks/rest/webhook` - Send messages
echo - GET `/status` - Check server status
echo - POST `/model/parse` - Parse text
) > deployment\README.md

echo.
echo Step 8: Creating test script...
(
echo import requests
echo import json
echo.
echo def test_rasa_api^(^):
echo     url = "http://localhost:5005/webhooks/rest/webhook"
echo     payload = {"sender": "test_user", "message": "Hello"}
echo     response = requests.post^(url, json=payload^)
echo     print^("Response:", response.json^(^)^)
echo.
echo if __name__ == "__main__":
echo     test_rasa_api^(^)
) > deployment\test_api.py

echo.
echo Step 9: Creating .env file...
(
echo RASA_MODEL_PATH=models/20250828-142409-sienna-specter.tar.gz
echo RASA_PORT=5005
echo ACTIONS_PORT=5055
) > deployment\.env

echo.
echo Step 10: Testing Rasa locally...
echo Starting Rasa server for testing...
start "Rasa Server" cmd /k "docker run --rm -v "%cd%\rasa:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005 --model models/20250828-142409-sienna-specter.tar.gz"

echo.
echo Waiting for server to start...
timeout /t 15 /nobreak >nul

echo.
echo Testing API...
powershell -Command "try { Invoke-RestMethod -Uri 'http://localhost:5005/status' -Method GET; Write-Host 'Rasa server is running!' } catch { Write-Host 'Server not ready yet...' }"

echo.
echo =========================================
echo    Deployment Package Created!
echo =========================================
echo.
echo Files created in 'deployment' folder:
echo - docker-compose.yml ^(Docker configuration^)
echo - deploy.sh ^(Deployment script^)
echo - README.md ^(Instructions^)
echo - test_api.py ^(API test script^)
echo - .env ^(Environment variables^)
echo.
echo To deploy to VPS:
echo 1. Upload the 'deployment' folder to your VPS
echo 2. SSH to your VPS
echo 3. Run: cd deployment ^&^& docker-compose up -d
echo.
echo Your Rasa bot will be available at:
echo - API: http://your-vps-ip:5005
echo - Actions: http://your-vps-ip:5055
echo.
echo Local test server is running on http://localhost:5005
echo.
pause
