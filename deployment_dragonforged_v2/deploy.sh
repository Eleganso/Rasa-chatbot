#!/bin/bash

echo "========================================="
echo "    Deploying DragonForgedDreams Bot V2"
echo "========================================="
echo.

# Update system
echo "Step 1: Updating system..."
sudo apt update && sudo apt upgrade -y

# Install Docker
echo "Step 2: Installing Docker..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    rm get-docker.sh
else
    echo "Docker already installed"
fi

# Install Docker Compose
echo "Step 3: Installing Docker Compose..."
if ! command -v docker-compose &> /dev/null; then
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
else
    echo "Docker Compose already installed"
fi

# Create SSL directory
echo "Step 4: Creating SSL directory..."
sudo mkdir -p ssl

# Generate self-signed certificate (replace with real certificate)
echo "Step 5: Generating SSL certificate..."
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout ssl/dragonforgeddreams.com.key \
    -out ssl/dragonforgeddreams.com.crt \
    -subj "/C=BG/ST=Sofia/L=Sofia/O=DragonForgedDreams/CN=dragonforgeddreams.com"

# Set proper permissions
sudo chmod 600 ssl/dragonforgeddreams.com.key
sudo chmod 644 ssl/dragonforgeddreams.com.crt

# Start services
echo "Step 6: Starting DragonForgedDreams Bot V2..."
sudo docker-compose up -d

# Wait for services to start
echo "Step 7: Waiting for services to start..."
sleep 30

# Test the bot
echo "Step 8: Testing DragonForgedDreams Bot V2..."
echo "Testing bot status..."
curl -s http://localhost:5005/status
echo.
echo "Testing web interface..."
curl -s -I http://localhost
echo.
echo "========================================="
echo "    DragonForgedDreams Bot V2 Deployed!"
echo "========================================="
echo.
echo "✅ Bot API: https://dragonforgeddreams.com/webhooks/rest/webhook"
echo "✅ Web Chat: https://dragonforgeddreams.com"
echo "✅ Bot Status: https://dragonforgeddreams.com/status"
echo.
echo "🔧 Management commands:"
echo "   - View logs: sudo docker-compose logs -f"
echo "   - Stop bot: sudo docker-compose down"
echo "   - Restart bot: sudo docker-compose restart"
echo "   - Update bot: sudo docker-compose pull && sudo docker-compose up -d"
echo.
echo "📝 Next steps:"
echo "   1. Replace self-signed certificate with real SSL certificate"
echo "   2. Configure domain DNS to point to this server"
echo "   3. Test the bot thoroughly"
echo "   4. Monitor logs for any issues"

