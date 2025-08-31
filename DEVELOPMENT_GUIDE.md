# 🐉 DragonForgedDreams Bot V2 - Development Guide

## 🤖 Текущ бот: DragonForgedDreams Bot V2

### 📍 Локация
- **Локално:** `bots/dragonforged_bot_v2/`
- **VPS:** `37.60.225.86` (активно разположен)
- **Модел:** `20250828-185711-shy-protagonist.tar.gz`

### 🎯 Функционалности
- **QR меню хостинг** - Информация за пакети и цени
- **Чатботове** - Създаване на ботове за сайтове и социални мрежи
- **Telegram ботове** - Автоматизация на бизнес процеси
- **Уебсайт разработка** - Модерни уебсайтове и PWA
- **SEO оптимизация** - Google класиране и видимост
- **Техническа поддръжка** - Консултации и поддръжка

## 🔧 How to Add New Intents

### 1. Add Training Examples
Edit `bots/dragonforged_bot_v2/rasa/data/nlu.yml` and add new intent:

```yaml
- intent: your_new_intent
  examples: |
    - example 1
    - example 2
    - example 3
    - пример 1
    - пример 2
    - пример 3
```

### 2. Add to Domain
Edit `bots/dragonforged_bot_v2/rasa/domain.yml` and add:
- intent name to intents list
- response in responses section

```yaml
intents:
  - your_new_intent

responses:
  utter_your_response:
    - text: "Вашият отговор тук"
    - text: "Your response here"
```

### 3. Add Stories
Edit `bots/dragonforged_bot_v2/rasa/data/stories.yml` and add conversation flow:

```yaml
- story: your story name
  steps:
  - intent: your_new_intent
  - action: utter_your_response
```

### 4. Train the Bot
```bash
# Локално
cd bots/dragonforged_bot_v2/rasa
docker run --rm -v "%cd%:/app" rasa/rasa:3.6.21 train --force

# Или използвайте скрипта
start_dragonforged_v2.bat
```

### 5. Test
```bash
# Локално тестване
start_dragonforged_v2.bat

# VPS тестване
curl -X POST http://37.60.225.86/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "your test message"}'
```

## 📋 Current Intents (12)

### 🎯 Основни интенти:
1. **greet** - Поздравления
   - "здравейте", "добър ден", "здрасти", "привет"
   - "hello", "hi", "good morning"

2. **ask_services** - Въпроси за услуги
   - "какво предлагате", "какви услуги имате", "с какво се занимавате"
   - "what do you offer", "what services do you have"

3. **ask_pricing** - Въпроси за цени
   - "колко струват услугите", "какви са цените", "тарифи"
   - "how much do services cost", "pricing"

4. **ask_qr_menu** - QR меню информация
   - "QR меню", "дигитално меню", "меню за ресторант"
   - "QR menu", "digital menu", "restaurant menu"

5. **ask_chatbots** - Въпроси за чатботове
   - "правите ли чатботове", "бот за сайта ми", "чатбот"
   - "do you make chatbots", "chatbot for my website"

6. **ask_website** - Въпроси за уебсайтове
   - "правите ли сайтове", "уебсайт", "онлайн магазин"
   - "do you make websites", "website", "online store"

7. **ask_seo** - SEO услуги
   - "SEO оптимизация", "Google класиране", "онлайн видимост"
   - "SEO optimization", "Google ranking", "online visibility"

8. **ask_telegram_bots** - Telegram ботове
   - "телеграм бот", "автоматизация", "бизнес процеси"
   - "telegram bot", "automation", "business processes"

9. **ask_pwa** - PWA приложения
   - "PWA", "мобилно приложение", "progressive web app"
   - "PWA", "mobile app", "progressive web app"

10. **ask_consultation** - Консултации
    - "консултация", "безплатна консултация", "съвет"
    - "consultation", "free consultation", "advice"

11. **ask_support** - Техническа поддръжка
    - "поддръжка", "техническа помощ", "support"
    - "support", "technical help", "maintenance"

12. **ask_contact** - Контактна информация
    - "как да се свържа", "контакт", "телефон"
    - "how to contact", "contact information", "phone"

## 🌍 Bilingual Support

Всички интенти поддържат **български и английски** език!

### Пример за двуезични отговори:
```yaml
responses:
  utter_greet:
    - text: "Здравейте! Добре дошли в DragonForged Dreams! Как мога да ви помогна днес?"
    - text: "Hello! Welcome to DragonForged Dreams! How can I help you today?"
```

## 🧪 Test Examples

### Български тестове:
- "Какво предлагате?"
- "Колко струват услугите ви?"
- "Правите ли чатботове?"
- "Искам QR меню за ресторанта ми"
- "Нужна ми е консултация"
- "Как да се свържа с вас?"

### English tests:
- "What do you offer?"
- "How much do your services cost?"
- "Do you make chatbots?"
- "I need a QR menu for my restaurant"
- "I need consultation"
- "How can I contact you?"

## 🚀 Deployment

### Локално стартиране:
```bash
start_dragonforged_v2.bat
```

### VPS deployment:
```bash
deploy_dragonforged_v2_to_vps.bat
```

### Проверка на статуса:
```bash
# Локално
curl http://localhost:5005/status

# VPS
curl http://37.60.225.86/status
```

## 📊 Performance

### Текущи ресурси на VPS:
- **RAM:** 12GB (използва се 12%)
- **CPU:** 6 cores (използва се 0%)
- **Диск:** 96GB NVMe (използва се 6%)
- **Rasa бот:** 792MB RAM

### Training време:
- **Локално:** ~45 секунди
- **VPS:** ~30 секунди (по-мощен хардуер)

## 🔄 Update Process

### 1. Локални промени
1. Редактирайте файловете в `bots/dragonforged_bot_v2/rasa/`
2. Тренирайте бота: `start_dragonforged_v2.bat`
3. Тествайте локално

### 2. VPS deployment
1. Създайте deployment пакет: `deploy_dragonforged_v2_to_vps.bat`
2. Качете на VPS
3. Изпълнете: `./deploy.sh`
4. Тествайте: `curl http://37.60.225.86/status`

## 📚 Useful Commands

```bash
# Проверка на модела
ls -la bots/dragonforged_bot_v2/rasa/models/

# Проверка на логовете
docker logs dragonforged-bot --tail 20

# Проверка на ресурсите
docker stats

# Backup на модела
cp bots/dragonforged_bot_v2/rasa/models/*.tar.gz backup/
```

---

**Последна актуализация:** 30 август 2025  
**Версия:** DragonForgedDreams Bot V2  
**Статус:** Активен на VPS (37.60.225.86)
