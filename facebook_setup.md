# Facebook Messenger Setup за Rasa

## 📋 Стъпки за настройване:

### 1. Създаване на Facebook App
1. Отидете на [Facebook Developers](https://developers.facebook.com/)
2. Създайте ново приложение
3. Изберете "Business" тип
4. Добавете "Messenger" продукт

### 2. Настройване на Page
1. Създайте Facebook страница (ако нямате)
2. В App Dashboard -> Messenger -> Settings
3. Свържете вашата страница
4. Запишете Page Access Token

### 3. Webhook настройване
1. В Messenger Settings -> Webhooks
2. Callback URL: `https://your-vps-ip:5005/webhooks/facebook/webhook`
3. Verify Token: `your_verify_token_here`
4. Subscribe to: `messages`, `messaging_postbacks`

### 4. Environment Variables
Добавете в `.env` файла:
```
FACEBOOK_ACCESS_TOKEN=your_page_access_token
FACEBOOK_VERIFY_TOKEN=your_verify_token
```

### 5. Rasa Credentials
В `credentials.yml`:
```yaml
facebook:
  verify: ${FACEBOOK_VERIFY_TOKEN}
  secret: ${FACEBOOK_SECRET}
  page-access-token: ${FACEBOOK_ACCESS_TOKEN}
```

## 🔧 Конфигурация за VPS:

### SSL сертификат (задължително за Facebook)
```bash
# Инсталиране на Certbot
sudo apt update
sudo apt install certbot

# SSL сертификат за вашия домейн
sudo certbot certonly --standalone -d your-domain.com
```

### Nginx конфигурация
```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;
    
    location / {
        proxy_pass http://localhost:5005;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## 🚀 Стартиране:
```bash
cd deployment
docker-compose up -d
```

## ✅ Тестване:
1. Отидете на вашата Facebook страница
2. Изпратете съобщение
3. Ботът трябва да отговори
