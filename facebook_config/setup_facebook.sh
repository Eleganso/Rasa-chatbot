#!/bin/bash
echo "Setting up Facebook Messenger for Rasa..."

echo "Step 1: Update .env file with your Facebook credentials"
echo "Edit facebook_config/.env and add your:"
echo "- FACEBOOK_ACCESS_TOKEN"
echo "- FACEBOOK_VERIFY_TOKEN" 
echo "- FACEBOOK_SECRET"

echo "Step 2: Get SSL certificate"
echo "sudo certbot certonly --standalone -d your-domain.com"

echo "Step 3: Copy SSL certificates"
echo "sudo cp /etc/letsencrypt/live/your-domain.com/fullchain.pem ./ssl/"
echo "sudo cp /etc/letsencrypt/live/your-domain.com/privkey.pem ./ssl/"

echo "Step 4: Start services"
echo "docker-compose up -d"

echo "Step 5: Configure Facebook Webhook"
echo "URL: https://your-domain.com/webhooks/facebook/webhook"
echo "Verify Token: your_verify_token_here"
