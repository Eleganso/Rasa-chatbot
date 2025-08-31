# 🌐 DragonForgedDreams Bot V2 - Website Integration

## ✅ Поправени проблеми:
- ✅ **Чат прозорецът сега се скролира автоматично до най-новите съобщения**
- ✅ **Работи с домейн без www** (dragonforgeddreams.com)

## 🔗 Активни линкове:
- **Основен URL:** http://37.60.225.86
- **API endpoint:** http://37.60.225.86/webhooks/rest/webhook
- **Статус:** http://37.60.225.86/status

## 🚀 Интеграция в сайта

### Вариант 1: Директен линк (Най-лесен)
Добавете този бутон в сайта:

```html
<a href="http://37.60.225.86" target="_blank" class="chat-button">
    💬 Чат с DragonForged Dreams
</a>
```

CSS за бутона:
```css
.chat-button {
    display: inline-block;
    padding: 12px 24px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-decoration: none;
    border-radius: 25px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.chat-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    color: white;
    text-decoration: none;
}
```

### Вариант 2: iframe интеграция
Добавете чата директно в страницата:

```html
<iframe 
    src="http://37.60.225.86" 
    width="100%" 
    height="600px" 
    frameborder="0"
    style="border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
</iframe>
```

### Вариант 3: Чат Widget (За напреднали)
Добавете този код в `<head>` секцията:

```html
<style>
.chat-widget {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 350px;
    height: 500px;
    background: white;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    z-index: 1000;
    display: none;
    flex-direction: column;
    overflow: hidden;
}

.chat-widget.active {
    display: flex;
}

.chat-toggle {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 60px;
    height: 60px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 50%;
    color: white;
    border: none;
    cursor: pointer;
    z-index: 1001;
    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
</style>
```

И JavaScript:
```javascript
const API_URL = 'http://37.60.225.86/webhooks/rest/webhook';

async function sendMessage(message) {
    try {
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                sender: 'user',
                message: message
            })
        });
        
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
```

## 🧪 Тестване

### Проверка на статуса:
```bash
curl http://37.60.225.86/status
```

### Тест на бота:
```bash
curl -X POST http://37.60.225.86/webhooks/rest/webhook \
  -H "Content-Type: application/json" \
  -d '{"sender": "test", "message": "Какво предлагате?"}'
```

## 📱 Responsive дизайн

Ботът вече има responsive дизайн и работи на:
- ✅ Desktop компютри
- ✅ Таблети  
- ✅ Мобилни телефони

## 🔒 Безопасност

- ✅ CORS е конфигуриран за всички домейни
- ✅ API е защитен с валидация
- ✅ HTTPS готов (трябва само SSL сертификат)

## 🎯 Функционалности

Ботът отговаря на въпроси за:
- **QR меню хостинг** - Пакети и цени
- **Чатботове** - Създаване на ботове
- **Telegram ботове** - Автоматизация
- **Уебсайт разработка** - Модерни сайтове
- **SEO оптимизация** - Google класиране
- **Техническа поддръжка** - Консултации

## 📞 Поддръжка

За въпроси и проблеми:
- Проверете статуса: http://37.60.225.86/status
- Тествайте API: http://37.60.225.86/webhooks/rest/webhook
- Уеб интерфейс: http://37.60.225.86

---

**✅ Готово за интеграция!** Просто използвайте линковете по-горе. 🚀
