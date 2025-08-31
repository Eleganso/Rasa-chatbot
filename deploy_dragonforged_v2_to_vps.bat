@echo off
echo =========================================
echo    Deploy DragonForgedDreams Bot V2 to VPS
echo =========================================
echo.
echo Step 1: Creating deployment package...
if exist deployment_dragonforged_v2 rmdir /s /q deployment_dragonforged_v2
mkdir deployment_dragonforged_v2
echo.
echo Step 2: Copying DragonForgedDreams Bot V2 files...
xcopy /e /i bots\dragonforged_bot_v2 deployment_dragonforged_v2\bot
echo.
echo Step 3: Creating docker-compose.yml for DragonForgedDreams Bot V2...
(
echo version: '3.8'
echo.
echo services:
echo   dragonforged-bot:
echo     image: rasa/rasa:3.6.21
echo     container_name: dragonforged-bot
echo     ports:
echo       - "5005:5005"
echo     volumes:
echo       - ./bot/rasa:/app
echo     command: run --enable-api --cors "*" --port 5005
echo     restart: unless-stopped
echo     environment:
echo       - RASA_TOKEN=${RASA_TOKEN:-}
echo.
echo   nginx:
echo     image: nginx:alpine
echo     container_name: dragonforged-nginx
echo     ports:
echo       - "80:80"
echo       - "443:443"
echo     volumes:
echo       - ./nginx.conf:/etc/nginx/nginx.conf
echo       - ./bot/web:/usr/share/nginx/html
echo       - ./ssl:/etc/nginx/ssl
echo     depends_on:
echo       - dragonforged-bot
echo     restart: unless-stopped
) > deployment_dragonforged_v2\docker-compose.yml
echo.
echo Step 4: Creating nginx.conf for DragonForgedDreams Bot V2...
(
echo events {
echo     worker_connections 1024;
echo }
echo.
echo http {
echo     upstream dragonforged_bot {
echo         server dragonforged-bot:5005;
echo     }
echo.
echo     server {
echo         listen 80;
echo         server_name dragonforgeddreams.com www.dragonforgeddreams.com;
echo.
echo         # Redirect HTTP to HTTPS
echo         return 301 https://$server_name$request_uri;
echo     }
echo.
echo     server {
echo         listen 443 ssl http2;
echo         server_name dragonforgeddreams.com www.dragonforgeddreams.com;
echo.
echo         # SSL Configuration
echo         ssl_certificate /etc/nginx/ssl/dragonforgeddreams.com.crt;
echo         ssl_certificate_key /etc/nginx/ssl/dragonforgeddreams.com.key;
echo         ssl_protocols TLSv1.2 TLSv1.3;
echo         ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
echo         ssl_prefer_server_ciphers off;
echo.
echo         # Security headers
echo         add_header X-Frame-Options DENY;
echo         add_header X-Content-Type-Options nosniff;
echo         add_header X-XSS-Protection "1; mode=block";
echo.
echo         # Serve static files (web chat interface)
echo         location / {
echo             root /usr/share/nginx/html;
echo             index index.html;
echo             try_files $uri $uri/ /index.html;
echo         }
echo.
echo         # Proxy API requests to Rasa bot
echo         location /webhooks/ {
echo             proxy_pass http://dragonforged_bot;
echo             proxy_set_header Host $host;
echo             proxy_set_header X-Real-IP $remote_addr;
echo             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
echo             proxy_set_header X-Forwarded-Proto $scheme;
echo             proxy_connect_timeout 30s;
echo             proxy_send_timeout 30s;
echo             proxy_read_timeout 30s;
echo         }
echo.
echo         # Proxy other Rasa endpoints
echo         location /model/ {
echo             proxy_pass http://dragonforged_bot;
echo             proxy_set_header Host $host;
echo             proxy_set_header X-Real-IP $remote_addr;
echo             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
echo             proxy_set_header X-Forwarded-Proto $scheme;
echo         }
echo.
echo         location /status {
echo             proxy_pass http://dragonforged_bot;
echo             proxy_set_header Host $host;
echo             proxy_set_header X-Real-IP $remote_addr;
echo             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
echo             proxy_set_header X-Forwarded-Proto $scheme;
echo         }
echo     }
echo }
) > deployment_dragonforged_v2\nginx.conf
echo.
echo Step 5: Creating deploy.sh for VPS...
(
echo #!/bin/bash
echo.
echo echo "========================================="
echo echo "    Deploying DragonForgedDreams Bot V2"
echo echo "========================================="
echo echo.
echo.
echo # Update system
echo echo "Step 1: Updating system..."
echo sudo apt update && sudo apt upgrade -y
echo.
echo # Install Docker
echo echo "Step 2: Installing Docker..."
echo if ! command -v docker &> /dev/null; then
echo     curl -fsSL https://get.docker.com -o get-docker.sh
echo     sudo sh get-docker.sh
echo     sudo usermod -aG docker $USER
echo     rm get-docker.sh
echo else
echo     echo "Docker already installed"
echo fi
echo.
echo # Install Docker Compose
echo echo "Step 3: Installing Docker Compose..."
echo if ! command -v docker-compose &> /dev/null; then
echo     sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
echo     sudo chmod +x /usr/local/bin/docker-compose
echo else
echo     echo "Docker Compose already installed"
echo fi
echo.
echo # Create SSL directory
echo echo "Step 4: Creating SSL directory..."
echo sudo mkdir -p ssl
echo.
echo # Generate self-signed certificate (replace with real certificate)
echo echo "Step 5: Generating SSL certificate..."
echo sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
echo     -keyout ssl/dragonforgeddreams.com.key \
echo     -out ssl/dragonforgeddreams.com.crt \
echo     -subj "/C=BG/ST=Sofia/L=Sofia/O=DragonForgedDreams/CN=dragonforgeddreams.com"
echo.
echo # Set proper permissions
echo sudo chmod 600 ssl/dragonforgeddreams.com.key
echo sudo chmod 644 ssl/dragonforgeddreams.com.crt
echo.
echo # Start services
echo echo "Step 6: Starting DragonForgedDreams Bot V2..."
echo sudo docker-compose up -d
echo.
echo # Wait for services to start
echo echo "Step 7: Waiting for services to start..."
echo sleep 30
echo.
echo # Test the bot
echo echo "Step 8: Testing DragonForgedDreams Bot V2..."
echo echo "Testing bot status..."
echo curl -s http://localhost:5005/status
echo echo.
echo echo "Testing web interface..."
echo curl -s -I http://localhost
echo echo.
echo echo "========================================="
echo echo "    DragonForgedDreams Bot V2 Deployed!"
echo echo "========================================="
echo echo.
echo echo "✅ Bot API: https://dragonforgeddreams.com/webhooks/rest/webhook"
echo echo "✅ Web Chat: https://dragonforgeddreams.com"
echo echo "✅ Bot Status: https://dragonforgeddreams.com/status"
echo echo.
echo echo "🔧 Management commands:"
echo echo "   - View logs: sudo docker-compose logs -f"
echo echo "   - Stop bot: sudo docker-compose down"
echo echo "   - Restart bot: sudo docker-compose restart"
echo echo "   - Update bot: sudo docker-compose pull && sudo docker-compose up -d"
echo echo.
echo echo "📝 Next steps:"
echo echo "   1. Replace self-signed certificate with real SSL certificate"
echo echo "   2. Configure domain DNS to point to this server"
echo echo "   3. Test the bot thoroughly"
echo echo "   4. Monitor logs for any issues"
) > deployment_dragonforged_v2\deploy.sh
echo.
echo Step 6: Creating README.md for DragonForgedDreams Bot V2...
(
echo # DragonForgedDreams Bot V2 - VPS Deployment
echo.
echo ## Overview
echo.
echo This is the deployment package for DragonForgedDreams Bot V2 - a specialized chatbot for dragonforgeddreams.com with detailed pricing and specific services focus.
echo.
echo ## Bot Features
echo.
echo - **13 specialized intents** covering all DragonForgedDreams services
echo - **QR Menu hosting** with detailed pricing packages
echo - **Telegram bots** for business automation
echo - **PWA applications** development
echo - **SEO optimization** services
echo - **Website development** with specific pricing
echo - **Technical support** with monthly pricing
echo - **Free consultation** offers
echo.
echo ## Services Covered
echo.
echo 1. **QR Menu Hosting** - 3 packages (Starter, Professional, Signature)
echo 2. **Chatbots** - Website and social media automation
echo 3. **Telegram Bots** - Business process automation
echo 4. **Website Development** - Modern, SEO-optimized websites
echo 5. **PWA Applications** - Progressive Web Apps
echo 6. **SEO Optimization** - Google ranking improvement
echo 7. **Technical Support** - 50 BGN/month professional support
echo.
echo ## Deployment Structure
echo.
echo ```
echo deployment_dragonforged_v2/
echo ├── bot/                    # DragonForgedDreams Bot V2 files
echo │   ├── rasa/              # Rasa configuration
echo │   │   ├── data/          # Training data
echo │   │   ├── models/        # Trained models
echo │   │   ├── config.yml     # Rasa configuration
echo │   │   ├── domain.yml     # Bot domain
echo │   │   ├── endpoints.yml  # API endpoints
echo │   │   └── credentials.yml # External channels
echo │   └── web/               # Web chat interface
echo │       └── index.html     # Chat UI
echo ├── docker-compose.yml     # Docker services
echo ├── nginx.conf            # Nginx configuration
echo ├── deploy.sh             # Deployment script
echo └── README.md             # This file
echo ```
echo.
echo ## Quick Start
echo.
echo 1. **Upload to VPS:**
echo    ```bash
echo    scp -r deployment_dragonforged_v2/ user@your-vps:/home/user/
echo    ```
echo.
echo 2. **SSH to VPS and deploy:**
echo    ```bash
echo    ssh user@your-vps
echo    cd deployment_dragonforged_v2
echo    chmod +x deploy.sh
echo    ./deploy.sh
echo    ```
echo.
echo 3. **Configure domain:**
echo    - Point dragonforgeddreams.com to your VPS IP
echo    - Replace self-signed certificate with real SSL certificate
echo.
echo ## API Endpoints
echo.
echo - **Bot API:** `https://dragonforgeddreams.com/webhooks/rest/webhook`
echo - **Status:** `https://dragonforgeddreams.com/status`
echo - **Web Chat:** `https://dragonforgeddreams.com`
echo.
echo ## Management Commands
echo.
echo ```bash
echo # View logs
echo sudo docker-compose logs -f
echo.
echo # Stop bot
echo sudo docker-compose down
echo.
echo # Restart bot
echo sudo docker-compose restart
echo.
echo # Update bot
echo sudo docker-compose pull && sudo docker-compose up -d
echo ```
echo.
echo ## Integration with Website
echo.
echo To integrate the bot into your existing website:
echo.
echo 1. **Add chat widget:**
echo    ```html
echo    <script>
echo    const BOT_API = 'https://dragonforgeddreams.com/webhooks/rest/webhook';
echo    // Your chat widget code here
echo    </script>
echo    ```
echo.
echo 2. **Or use iframe:**
echo    ```html
echo    <iframe src="https://dragonforgeddreams.com" 
echo            width="400" height="600" 
echo            style="border: none;">
echo    </iframe>
echo    ```
echo.
echo ## Monitoring
echo.
echo - Check bot status: `curl https://dragonforgeddreams.com/status`
echo - Monitor logs: `sudo docker-compose logs -f dragonforged-bot`
echo - Check nginx: `sudo docker-compose logs -f nginx`
echo.
echo ## Troubleshooting
echo.
echo **Bot not responding:**
echo - Check if containers are running: `sudo docker-compose ps`
echo - Check bot logs: `sudo docker-compose logs dragonforged-bot`
echo - Verify port 5005 is accessible
echo.
echo **SSL issues:**
echo - Replace self-signed certificate with real certificate
echo - Update nginx.conf with correct certificate paths
echo - Restart nginx: `sudo docker-compose restart nginx`
echo.
echo **Domain not working:**
echo - Verify DNS settings point to VPS IP
echo - Check nginx configuration
echo - Test with IP address first
echo.
echo ## Support
echo.
echo For technical support or questions about DragonForgedDreams Bot V2, contact:
echo - Email: info@dragonforgeddreams.com
echo - Website: https://dragonforgeddreams.com
echo.
echo ---
echo *DragonForgedDreams Bot V2 - Professional chatbot for dragonforgeddreams.com*
) > deployment_dragonforged_v2\README.md
echo.
echo Step 7: Creating .env file for environment variables...
(
echo # DragonForgedDreams Bot V2 Environment Variables
echo.
echo # Rasa Configuration
echo RASA_TOKEN=your_rasa_token_here
echo.
echo # Domain Configuration
echo DOMAIN_NAME=dragonforgeddreams.com
echo.
echo # SSL Configuration
echo SSL_CERT_PATH=/etc/nginx/ssl/dragonforgeddreams.com.crt
echo SSL_KEY_PATH=/etc/nginx/ssl/dragonforgeddreams.com.key
echo.
echo # Bot Configuration
echo BOT_NAME=DragonForgedDreams Bot V2
echo BOT_DESCRIPTION=Professional chatbot for dragonforgeddreams.com services
) > deployment_dragonforged_v2\.env
echo.
echo Step 8: Creating test script...
(
echo #!/bin/bash
echo.
echo echo "Testing DragonForgedDreams Bot V2..."
echo echo.
echo.
echo # Test bot status
echo echo "1. Testing bot status..."
echo response=$(curl -s http://localhost:5005/status)
echo if [[ $response == *"status"* ]]; then
echo     echo "✅ Bot is running"
echo else
echo     echo "❌ Bot is not responding"
echo fi
echo echo.
echo.
echo # Test web interface
echo echo "2. Testing web interface..."
echo response=$(curl -s -I http://localhost | head -1)
echo if [[ $response == *"200"* ]]; then
echo     echo "✅ Web interface is accessible"
echo else
echo     echo "❌ Web interface is not accessible"
echo fi
echo echo.
echo.
echo # Test bot API
echo echo "3. Testing bot API..."
echo response=$(curl -s -X POST http://localhost:5005/webhooks/rest/webhook \
echo     -H "Content-Type: application/json" \
echo     -d '{"message": "здравейте", "sender": "test_user"}')
echo if [[ $response == *"text"* ]]; then
echo     echo "✅ Bot API is working"
echo     echo "Response: $response"
echo else
echo     echo "❌ Bot API is not working"
echo fi
echo echo.
echo.
echo echo "========================================="
echo echo "    DragonForgedDreams Bot V2 Test Complete"
echo echo "========================================="
) > deployment_dragonforged_v2\test_bot.sh
echo.
echo Step 9: Making scripts executable...
echo chmod +x deployment_dragonforged_v2\deploy.sh
echo chmod +x deployment_dragonforged_v2\test_bot.sh
echo.
echo =========================================
echo    DragonForgedDreams Bot V2 Deployment Package Ready!
echo =========================================
echo.
echo 📦 Package created: deployment_dragonforged_v2/
echo.
echo 📋 Contents:
echo    ✅ DragonForgedDreams Bot V2 files
echo    ✅ docker-compose.yml
echo    ✅ nginx.conf (SSL ready)
echo    ✅ deploy.sh (automated deployment)
echo    ✅ test_bot.sh (testing script)
echo    ✅ README.md (documentation)
echo    ✅ .env (environment variables)
echo.
echo 🚀 Next steps:
echo    1. Upload deployment_dragonforged_v2/ to your VPS
echo    2. SSH to VPS and run: cd deployment_dragonforged_v2 && ./deploy.sh
echo    3. Configure your domain DNS
echo    4. Replace SSL certificate with real one
echo    5. Test the bot thoroughly
echo.
echo 🌐 Bot will be available at:
echo    - https://dragonforgeddreams.com (web chat)
echo    - https://dragonforgeddreams.com/webhooks/rest/webhook (API)
echo.
pause

