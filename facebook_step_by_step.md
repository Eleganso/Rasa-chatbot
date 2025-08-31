# Facebook Messenger Setup - Стъпка по стъпка

## 🎯 Цел: Настроите Rasa бота да работи във Facebook Messenger

---

## 📋 Предварителни изисквания:
- VPS с домейн (например: your-bot.com)
- Docker инсталиран на VPS
- Facebook акаунт

---

## 🚀 Стъпка 1: Създаване на Facebook App

### 1.1 Отидете на Facebook Developers
- Отворете: https://developers.facebook.com/
- Влезте с вашия Facebook акаунт

### 1.2 Създайте ново приложение
- Кликнете "Create App"
- Изберете "Business" тип
- Въведете име на приложението (например: "My Rasa Bot")
- Кликнете "Create App"

### 1.3 Добавете Messenger продукт
- В App Dashboard кликнете "Add Product"
- Намерете "Messenger" и кликнете "Set Up"

---

## 🚀 Стъпка 2: Създаване на Facebook Page

### 2.1 Създайте страница (ако нямате)
- Отидете на: https://www.facebook.com/pages/create
- Изберете тип страница (например: "Business or Brand")
- Въведете име на страницата
- Следвайте стъпките за създаване

### 2.2 Свържете страницата с приложението
- В App Dashboard -> Messenger -> Settings
- В секцията "Access Tokens" кликнете "Add or Remove Pages"
- Изберете вашата страница
- Кликнете "Add Page"
- **ВАЖНО**: Запишете Page Access Token!

---

## 🚀 Стъпка 3: Настройване на Webhook

### 3.1 В Messenger Settings
- Отидете в App Dashboard -> Messenger -> Settings
- Скролирайте до "Webhooks" секцията
- Кликнете "Add Callback URL"

### 3.2 Конфигурирайте Webhook
- **Callback URL**: `https://your-domain.com/webhooks/facebook/webhook`
- **Verify Token**: `your_secret_token_here` (измислете сложен токен)
- **Subscription Fields**: Изберете:
  - ✅ `messages`
  - ✅ `messaging_postbacks`
  - ✅ `messaging_optins`
  - ✅ `message_deliveries`
  - ✅ `message_reads`

### 3.3 Запишете App Secret
- В App Dashboard -> Settings -> Basic
- Запишете App Secret

---

## 🚀 Стъпка 4: Подготовка на VPS

### 4.1 Качете файловете
```bash
# Качете facebook_config папката на вашия VPS
scp -r facebook_config/ user@your-vps-ip:/home/user/
```

### 4.2 SSH към VPS
```bash
ssh user@your-vps-ip
cd facebook_config
```

### 4.3 Редактирайте .env файла
```bash
nano .env
```

Добавете вашите Facebook данни:
```env
# Facebook Messenger Configuration
FACEBOOK_ACCESS_TOKEN=your_page_access_token_here
FACEBOOK_VERIFY_TOKEN=your_verify_token_here
FACEBOOK_SECRET=your_app_secret_here

# Rasa Configuration
RASA_MODEL_PATH=models/20250828-142409-sienna-specter.tar.gz
RASA_PORT=5005
ACTIONS_PORT=5055
```

---

## 🚀 Стъпка 5: SSL сертификат

### 5.1 Инсталирайте Certbot
```bash
sudo apt update
sudo apt install certbot
```

### 5.2 Получете SSL сертификат
```bash
sudo certbot certonly --standalone -d your-domain.com
```

### 5.3 Копирайте сертификатите
```bash
sudo cp /etc/letsencrypt/live/your-domain.com/fullchain.pem ./ssl/
sudo cp /etc/letsencrypt/live/your-domain.com/privkey.pem ./ssl/
sudo chown $USER:$USER ./ssl/*
```

---

## 🚀 Стъпка 6: Стартиране на бота

### 6.1 Стартирайте Docker контейнерите
```bash
docker-compose up -d
```

### 6.2 Проверете статуса
```bash
docker-compose ps
docker-compose logs rasa
```

---

## 🚀 Стъпка 7: Тестване

### 7.1 Проверете webhook
```bash
curl -X GET "https://your-domain.com/webhooks/facebook/webhook?hub.mode=subscribe&hub.challenge=test&hub.verify_token=your_verify_token"
```

### 7.2 Тествайте в Facebook
- Отидете на вашата Facebook страница
- Кликнете "Message"
- Изпратете съобщение "Hello"
- Ботът трябва да отговори!

---

## 🔧 Troubleshooting

### Проблем: Webhook не работи
**Решение:**
1. Проверете дали домейнът сочи към VPS
2. Проверете дали порт 443 е отворен
3. Проверете SSL сертификата

### Проблем: Ботът не отговаря
**Решение:**
1. Проверете логовете: `docker-compose logs rasa`
2. Проверете дали токените са правилни
3. Проверете дали webhook URL е правилен

### Проблем: SSL грешка
**Решение:**
1. Обновете сертификата: `sudo certbot renew`
2. Копирайте новите сертификати
3. Рестартирайте контейнерите

---

## 📞 Поддръжка

За проблеми:
1. Проверете логовете: `docker-compose logs`
2. Тествайте webhook URL
3. Проверете Facebook App настройките
4. Уверете се, че домейнът работи

---

## ✅ Успешно настройване!

След тези стъпки вашият Rasa бот ще работи във Facebook Messenger! 🎉
