# 🐉 DragonForgedDreams Bot V2 - Rasa VPS Deployment

Този проект съдържа напълно функционален DragonForgedDreams Bot V2, готов за deployment на VPS.

## 🚀 Текущо състояние

### ✅ Активно разположен:
- **VPS:** Contabo Cloud VPS 20 (37.60.225.86)
- **Ресурси:** 12GB RAM, 6 CPU cores, 96GB NVMe
- **Статус:** Работи стабилно
- **URL:** http://37.60.225.86

### 📊 Ресурси:
- **RAM използване:** 12% (1.4GB от 11.7GB)
- **Диск използване:** 6% (5.6GB от 96GB)
- **CPU натоварване:** 0.00%
- **Rasa бот:** 792MB RAM, 6.62%

## 🚀 Бърз старт

### Локално тестване:
1. Стартирайте `start_dragonforged_v2.bat` за локално тестване
2. Стартирайте `start_dragonforged_bots.bat` за dashboard
3. Rasa сървърът ще бъде достъпен на `http://localhost:5005`

### VPS Deployment:
1. Използвайте `deploy_dragonforged_v2_to_vps.bat` за създаване на deployment пакета
2. Качете `deployment_dragonforged_v2/` папката на вашия VPS
3. SSH към VPS и изпълнете:
   ```bash
   cd deployment_dragonforged_v2
   chmod +x deploy.sh
   ./deploy.sh
   ```
4. Вашият бот ще бъде достъпен на `http://your-vps-ip`

## 📁 Структура на проекта

```
Rasa VPS/
├── bots/                           # Всички ботове
│   ├── dragonforged_bot_v1/        # DragonForgedDreams Bot V1
│   ├── dragonforged_bot_v2/        # DragonForgedDreams Bot V2 (активен)
│   ├── customer_service_bot/       # Customer Service Bot
│   ├── hr_bot/                     # HR Bot
│   ├── sales_bot/                  # Sales Bot
│   ├── tech_support_bot/           # Tech Support Bot
│   └── tourism_bot/                # Tourism Bot
├── deployment_dragonforged_v2/     # Deployment пакет за V2
│   ├── docker-compose.yml         # Docker конфигурация
│   ├── deploy.sh                  # Deployment скрипт
│   ├── nginx.conf                 # Nginx конфигурация
│   └── bot/                       # Rasa бот файлове
├── create_dragonforged_bot_v2.py  # Скрипт за създаване на V2 бот
├── start_dragonforged_v2.bat      # Стартиране на V2 бот
├── deploy_dragonforged_v2_to_vps.bat # Deployment скрипт
└── website_integration_guide.md   # Интеграция в уебсайт
```

## 🤖 DragonForgedDreams Bot V2

### Функционалности:
- **QR меню хостинг** - Информация за пакети и цени
- **Чатботове** - Създаване на ботове за сайтове и социални мрежи
- **Telegram ботове** - Автоматизация на бизнес процеси
- **Уебсайт разработка** - Модерни уебсайтове и PWA
- **SEO оптимизация** - Google класиране и видимост
- **Техническа поддръжка** - Консултации и поддръжка

### Интенти:
- **greet** - Поздравления
- **ask_services** - Въпроси за услуги
- **ask_pricing** - Въпроси за цени
- **ask_qr_menu** - QR меню информация
- **ask_chatbots** - Въпроси за чатботове
- **ask_website** - Въпроси за уебсайтове
- **ask_seo** - SEO услуги
- **ask_telegram_bots** - Telegram ботове
- **ask_pwa** - PWA приложения
- **ask_consultation** - Консултации
- **ask_support** - Техническа поддръжка
- **ask_contact** - Контактна информация

## 🔧 API Endpoints

- `POST /webhooks/rest/webhook` - Изпращане на съобщения
- `GET /status` - Статус на сървъра
- `POST /model/parse` - Парсване на текст

### Пример за използване:
```bash
curl -X POST http://37.60.225.86/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "user", "message": "Какво предлагате?"}'
```

## 🐳 Docker

Проектът използва Docker за лесен deployment:
- **Rasa Server**: `rasa/rasa:3.6.21` на порт 5005
- **Nginx**: `nginx:alpine` на порт 80/443

### Контейнери:
- **dragonforged-bot**: Rasa бот сървър
- **dragonforged-nginx**: Nginx уеб сървър

## 📊 Статистики

- **Модел**: `20250828-185711-shy-protagonist.tar.gz` (27MB)
- **Rasa версия**: 3.6.21
- **Python версия**: 3.10 (в Docker контейнера)
- **Training време**: ~45 секунди
- **VPS ресурси**: 12GB RAM, 6 CPU cores, 96GB NVMe

## 🌐 Уеб интерфейс

- **URL**: http://37.60.225.86
- **Функции**: Чат интерфейс, API достъп
- **Дизайн**: Модерен, responsive дизайн
- **Езици**: Български и английски

## 🔄 Следващи стъпки

1. **Домейн**: Настройте dragonforgeddreams.com
2. **SSL**: Добавете SSL сертификат
3. **Интеграция**: Свържете с уебсайта
4. **Мониторинг**: Добавете logging и monitoring
5. **Backup**: Настройте автоматични backups

## 📞 Поддръжка

За въпроси и проблеми:
- Проверете логовете: `docker logs dragonforged-bot`
- Тествайте API: `curl http://37.60.225.86/status`
- Проверете ресурсите: `docker stats`
- Уеб интерфейс: http://37.60.225.86

## 📚 Документация

- [DEVELOPMENT_GUIDE.md](DEVELOPMENT_GUIDE.md) - Как да добавите нови интенти
- [website_integration_guide.md](website_integration_guide.md) - Интеграция в уебсайт
- [facebook_setup.md](facebook_setup.md) - Facebook Messenger интеграция

## 🎯 Резултати

✅ **Успешно разположен** DragonForgedDreams Bot V2 на мощен VPS  
✅ **Стабилна работа** с 85% свободни ресурси  
✅ **Модерен уеб интерфейс** с чат функционалност  
✅ **Готов за интеграция** в уебсайт  
✅ **Масштабируемо решение** за бъдещо развитие
