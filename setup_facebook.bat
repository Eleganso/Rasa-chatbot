@echo off
echo =========================================
echo    Facebook Messenger Setup
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
echo Step 3: Creating Facebook configuration...
if not exist "facebook_config" mkdir facebook_config

echo.
echo Step 4: Creating .env file with Facebook variables...
(
echo # Facebook Messenger Configuration
echo FACEBOOK_ACCESS_TOKEN=your_page_access_token_here
echo FACEBOOK_VERIFY_TOKEN=your_verify_token_here
echo FACEBOOK_SECRET=your_app_secret_here
echo.
echo # Rasa Configuration
echo RASA_MODEL_PATH=models/20250828-142409-sienna-specter.tar.gz
echo RASA_PORT=5005
echo ACTIONS_PORT=5055
) > facebook_config\.env

echo.
echo Step 5: Creating Facebook deployment docker-compose...
(
echo version: '3.8'
echo services:
echo   rasa:
echo     image: rasa/rasa:3.6.21
echo     ports:
echo       - "5005:5005"
echo     volumes:
echo       - ./rasa:/app
echo     environment:
echo       - FACEBOOK_ACCESS_TOKEN=${FACEBOOK_ACCESS_TOKEN}
echo       - FACEBOOK_VERIFY_TOKEN=${FACEBOOK_VERIFY_TOKEN}
echo       - FACEBOOK_SECRET=${FACEBOOK_SECRET}
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
echo.
echo   nginx:
echo     image: nginx:alpine
echo     ports:
echo       - "80:80"
echo       - "443:443"
echo     volumes:
echo       - ./nginx.conf:/etc/nginx/nginx.conf
echo       - ./ssl:/etc/nginx/ssl
echo     depends_on:
echo       - rasa
echo     restart: unless-stopped
) > facebook_config\docker-compose.yml

echo.
echo Step 6: Creating Nginx configuration...
(
echo events {
echo     worker_connections 1024;
echo }
echo.
echo http {
echo     upstream rasa {
echo         server rasa:5005;
echo     }
echo.
echo     server {
echo         listen 80;
echo         server_name your-domain.com;
echo         return 301 https://$server_name$request_uri;
echo     }
echo.
echo     server {
echo         listen 443 ssl;
echo         server_name your-domain.com;
echo.
echo         ssl_certificate /etc/nginx/ssl/fullchain.pem;
echo         ssl_certificate_key /etc/nginx/ssl/privkey.pem;
echo.
echo         location / {
echo             proxy_pass http://rasa;
echo             proxy_set_header Host $host;
echo             proxy_set_header X-Real-IP $remote_addr;
echo             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
echo             proxy_set_header X-Forwarded-Proto $scheme;
echo         }
echo     }
echo }
) > facebook_config\nginx.conf

echo.
echo Step 7: Creating Facebook setup script...
(
echo #!/bin/bash
echo echo "Setting up Facebook Messenger for Rasa..."
echo.
echo echo "Step 1: Update .env file with your Facebook credentials"
echo echo "Edit facebook_config/.env and add your:"
echo echo "- FACEBOOK_ACCESS_TOKEN"
echo echo "- FACEBOOK_VERIFY_TOKEN" 
echo echo "- FACEBOOK_SECRET"
echo.
echo echo "Step 2: Get SSL certificate"
echo echo "sudo certbot certonly --standalone -d your-domain.com"
echo.
echo echo "Step 3: Copy SSL certificates"
echo echo "sudo cp /etc/letsencrypt/live/your-domain.com/fullchain.pem ./ssl/"
echo echo "sudo cp /etc/letsencrypt/live/your-domain.com/privkey.pem ./ssl/"
echo.
echo echo "Step 4: Start services"
echo echo "docker-compose up -d"
echo.
echo echo "Step 5: Configure Facebook Webhook"
echo echo "URL: https://your-domain.com/webhooks/facebook/webhook"
echo echo "Verify Token: your_verify_token_here"
) > facebook_config\setup_facebook.sh

echo.
echo Step 8: Copying Rasa files...
xcopy "rasa\*" "facebook_config\rasa\" /E /I /Y

echo.
echo Step 9: Creating SSL directory...
if not exist "facebook_config\ssl" mkdir facebook_config\ssl

echo.
echo =========================================
echo    Facebook Setup Complete!
echo =========================================
echo.
echo Next steps:
echo 1. Go to https://developers.facebook.com/
echo 2. Create a new app and add Messenger
echo 3. Create a Facebook page
echo 4. Get your Page Access Token
echo 5. Edit facebook_config/.env with your tokens
echo 6. Get SSL certificate for your domain
echo 7. Run: cd facebook_config ^&^& docker-compose up -d
echo.
echo Facebook Webhook URL:
echo https://your-domain.com/webhooks/facebook/webhook
echo.
echo Verify Token: your_verify_token_here
echo.
pause
