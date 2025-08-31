# DragonForgedDreams Bot V2 - VPS Deployment

## Overview

This is the deployment package for DragonForgedDreams Bot V2 - a specialized chatbot for dragonforgeddreams.com with detailed pricing and specific services focus.

## Bot Features

- **13 specialized intents** covering all DragonForgedDreams services
- **QR Menu hosting** with detailed pricing packages
- **Telegram bots** for business automation
- **PWA applications** development
- **SEO optimization** services
- **Website development** with specific pricing
- **Technical support** with monthly pricing
- **Free consultation** offers

## Services Covered

1. **QR Menu Hosting** - 3 packages (Starter, Professional, Signature)
2. **Chatbots** - Website and social media automation
3. **Telegram Bots** - Business process automation
4. **Website Development** - Modern, SEO-optimized websites
5. **PWA Applications** - Progressive Web Apps
6. **SEO Optimization** - Google ranking improvement
7. **Technical Support** - 50 BGN/month professional support

## Deployment Structure

```
deployment_dragonforged_v2/
├── bot/                    # DragonForgedDreams Bot V2 files
│   ├── rasa/              # Rasa configuration
│   │   ├── data/          # Training data
│   │   ├── models/        # Trained models
│   │   ├── config.yml     # Rasa configuration
│   │   ├── domain.yml     # Bot domain
│   │   ├── endpoints.yml  # API endpoints
│   │   └── credentials.yml # External channels
│   └── web/               # Web chat interface
│       └── index.html     # Chat UI
├── docker-compose.yml     # Docker services
├── nginx.conf            # Nginx configuration
├── deploy.sh             # Deployment script
└── README.md             # This file
```

## Quick Start

1. **Upload to VPS:**
   ```bash
   scp -r deployment_dragonforged_v2/ user@your-vps:/home/user/
   ```

2. **SSH to VPS and deploy:**
   ```bash
   ssh user@your-vps
   cd deployment_dragonforged_v2
   chmod +x deploy.sh
   ./deploy.sh
   ```

3. **Configure domain:**
   - Point dragonforgeddreams.com to your VPS IP
   - Replace self-signed certificate with real SSL certificate

## API Endpoints

- **Bot API:** `https://dragonforgeddreams.com/webhooks/rest/webhook`
- **Status:** `https://dragonforgeddreams.com/status`
- **Web Chat:** `https://dragonforgeddreams.com`

## Management Commands

```bash
# View logs
sudo docker-compose logs -f

# Stop bot
sudo docker-compose down

# Restart bot
sudo docker-compose restart

# Update bot
sudo docker-compose pull && sudo docker-compose up -d
```

## Integration with Website

To integrate the bot into your existing website:

1. **Add chat widget:**
   ```html
   <script>
   const BOT_API = 'https://dragonforgeddreams.com/webhooks/rest/webhook';
   // Your chat widget code here
   </script>
   ```

2. **Or use iframe:**
   ```html
   <iframe src="https://dragonforgeddreams.com" 
           width="400" height="600" 
           style="border: none;">
   </iframe>
   ```

## Monitoring

- Check bot status: `curl https://dragonforgeddreams.com/status`
- Monitor logs: `sudo docker-compose logs -f dragonforged-bot`
- Check nginx: `sudo docker-compose logs -f nginx`

## Troubleshooting

**Bot not responding:**
- Check if containers are running: `sudo docker-compose ps`
- Check bot logs: `sudo docker-compose logs dragonforged-bot`
- Verify port 5005 is accessible

**SSL issues:**
- Replace self-signed certificate with real certificate
- Update nginx.conf with correct certificate paths
- Restart nginx: `sudo docker-compose restart nginx`

**Domain not working:**
- Verify DNS settings point to VPS IP
- Check nginx configuration
- Test with IP address first

## Support

For technical support or questions about DragonForgedDreams Bot V2, contact:
- Email: info@dragonforgeddreams.com
- Website: https://dragonforgeddreams.com

---

*DragonForgedDreams Bot V2 - Professional chatbot for dragonforgeddreams.com*

