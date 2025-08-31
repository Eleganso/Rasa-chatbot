# 🚀 DragonForgedDreams Bot V2 - Quick Commands

## 📍 Активен VPS
- **IP:** 37.60.225.86
- **URL:** http://37.60.225.86
- **Статус:** Активен

## 🔧 Основни команди

### 📊 Проверка на ресурсите
```bash
# RAM и диск
ssh root@37.60.225.86 "free -h && df -h"

# CPU и натоварване
ssh root@37.60.225.86 "uptime"

# Docker контейнери
ssh root@37.60.225.86 "docker ps && docker stats --no-stream"
```

### 🐳 Docker управление
```bash
# Проверка на контейнерите
ssh root@37.60.225.86 "docker ps"

# Рестартиране на бота
ssh root@37.60.225.86 "docker restart dragonforged-bot"

# Рестартиране на nginx
ssh root@37.60.225.86 "docker restart dragonforged-nginx"

# Рестартиране на всички
ssh root@37.60.225.86 "cd /root/dragonforged_bot && docker-compose restart"
```

### 📝 Логове
```bash
# Rasa логове
ssh root@37.60.225.86 "docker logs dragonforged-bot --tail 20"

# Nginx логове
ssh root@37.60.225.86 "docker logs dragonforged-nginx --tail 20"

# Системни логове
ssh root@37.60.225.86 "tail -20 /var/log/syslog"
```

### 🧪 Тестване
```bash
# Проверка на статуса
ssh root@37.60.225.86 "curl http://localhost:5005/status"

# Тест на бота
ssh root@37.60.225.86 "curl -X POST http://localhost:5005/webhooks/rest/webhook -H 'Content-Type: application/json' -d '{\"sender\":\"test\",\"message\":\"здравейте\"}'"

# Тест на уеб интерфейса
ssh root@37.60.225.86 "curl http://localhost:80"
```

## 🚀 Локално развитие

### 📁 Файлове за редактиране
```
bots/dragonforged_bot_v2/rasa/
├── data/
│   ├── nlu.yml          # Training примери
│   ├── stories.yml      # Разговорни потоци
│   └── rules.yml        # Правила
├── domain.yml           # Интенти и отговори
├── config.yml           # Rasa конфигурация
└── models/              # Тренирани модели
```

### 🔄 Training процес
```bash
# Локално training
cd bots/dragonforged_bot_v2/rasa
docker run --rm -v "%cd%:/app" rasa/rasa:3.6.21 train --force

# Или използвайте скрипта
start_dragonforged_v2.bat
```

### 🧪 Локално тестване
```bash
# Стартиране на бота
start_dragonforged_v2.bat

# Тестване
curl -X POST http://localhost:5005/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "здравейте"}'
```

## 📤 Deployment

### 🚀 VPS deployment
```bash
# 1. Създаване на deployment пакет
deploy_dragonforged_v2_to_vps.bat

# 2. Качване на VPS
scp -r deployment_dragonforged_v2/* root@37.60.225.86:/root/dragonforged_bot/

# 3. Стартиране на VPS
ssh root@37.60.225.86 "cd /root/dragonforged_bot && docker-compose up -d"
```

### 🔄 Update на VPS
```bash
# 1. Спиране на контейнерите
ssh root@37.60.225.86 "cd /root/dragonforged_bot && docker-compose down"

# 2. Качване на нови файлове
scp -r bots/dragonforged_bot_v2/* root@37.60.225.86:/root/dragonforged_bot/

# 3. Стартиране отново
ssh root@37.60.225.86 "cd /root/dragonforged_bot && docker-compose up -d"
```

## 📊 Мониторинг

### 📈 Ресурси
```bash
# Проверка на паметта
ssh root@37.60.225.86 "free -h"

# Проверка на диска
ssh root@37.60.225.86 "df -h"

# Проверка на процесите
ssh root@37.60.225.86 "ps aux --sort=-%mem | head -10"
```

### 🔍 Проблеми
```bash
# Проверка на портове
ssh root@37.60.225.86 "netstat -tulpn | grep -E '(80|5005)'"

# Проверка на мрежата
ssh root@37.60.225.86 "ping -c 3 google.com"

# Проверка на Docker
ssh root@37.60.225.86 "docker system df"
```

## 🛠️ Backup

### 💾 Backup на модела
```bash
# Локално
cp bots/dragonforged_bot_v2/rasa/models/*.tar.gz backup/

# VPS
ssh root@37.60.225.86 "cp /root/dragonforged_bot/rasa/models/*.tar.gz /backup/"
```

### 📁 Backup на конфигурациите
```bash
# Локално
cp -r bots/dragonforged_bot_v2/rasa/ backup/rasa_config/

# VPS
ssh root@37.60.225.86 "cp -r /root/dragonforged_bot/rasa/ /backup/rasa_config/"
```

## 🎯 Бързи тестове

### ✅ Проверка на статуса
```bash
# VPS статус
curl http://37.60.225.86/status

# Бот статус
curl http://37.60.225.86:5005/status
```

### 💬 Тест на чата
```bash
# Български
curl -X POST http://37.60.225.86/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "Какво предлагате?"}'

# English
curl -X POST http://37.60.225.86/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "What do you offer?"}'
```

## 📞 Поддръжка

### 🆘 Аварийни команди
```bash
# Рестартиране на всичко
ssh root@37.60.225.86 "reboot"

# Проверка на логовете след рестартиране
ssh root@37.60.225.86 "docker logs dragonforged-bot --tail 50"

# Проверка на ресурсите след рестартиране
ssh root@37.60.225.86 "free -h && df -h"
```

---

**💡 Съвет:** Забравете паролата? Използвайте VNC: `213.136.68.205:63267`  
**📧 Контакт:** За въпроси и проблеми  
**🔄 Последна актуализация:** 30 август 2025
