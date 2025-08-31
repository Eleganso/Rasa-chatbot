# 🤖 МУЛТИ-БОТ СИСТЕМА - ЛОКАЛНО ТЕСТВАНЕ

## 📋 Описание
Ръководство за локално тестване на всички 6 Rasa бота с Docker контейнери и динамични web интерфейси.

## 🚀 Бързо стартиране

### ⚠️ Важно:
- **Стартирайте само един бот наведнъж** (за да избегнете конфликти на портове)
- **Изчакайте 15-20 секунди** след стартиране преди тестване
- **Спрете бота** преди да стартирате друг
- **Web интерфейсите се отварят автоматично** в браузъра

## 🌟 Нови функции

### 🔄 **Динамични web интерфейси**
- **Автоматично адаптиране** за локално/VPS среда
- **Проверка на връзката** в реално време
- **Модерен дизайн** с индивидуални цветове за всеки бот
- **Отваряне автоматично** в браузъра

### 🎯 **Как работи:**
- **Локално:** `localhost:5005` → `http://localhost:5005/webhooks/rest/webhook`
- **VPS:** `37.60.225.86/dragonforged-v2` → `/dragonforged-v2/webhooks/rest/webhook`
- **Един код, две среди** - автоматично се адаптира

## 🤖 Списък с ботове

### 1️⃣ **DragonForgedDreams V2** (Порт 5005)
```bash
docker run -v ${PWD}/bots/dragonforged_bot_v2/rasa:/app -p 5005:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5005/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5005`
**Цвят:** 🟤 Кафяв

### 2️⃣ **Салон "Златна коса"** (Порт 5006)
```bash
docker run -v ${PWD}/bots/zlatna_kosa_salon/rasa:/app -p 5006:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5006/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5006`
**Цвят:** 🟡 Златен

### 3️⃣ **Ресторант "Златна вилица"** (Порт 5007)
```bash
docker run -v ${PWD}/bots/zlatna_vilitsa_restaurant/rasa:/app -p 5007:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5007/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5007`
**Цвят:** 🟠 Оранжев

### 4️⃣ **Хотел "Гранд София"** (Порт 5008)
```bash
docker run -v ${PWD}/bots/grand_sofia_hotel/rasa:/app -p 5008:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5008/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5008`
**Цвят:** 🔵 Син

### 5️⃣ **Медицински център "Здраве+"** (Порт 5009)
```bash
docker run -v ${PWD}/bots/zdrave_medical_center/rasa:/app -p 5009:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5009/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5009`
**Цвят:** 🟢 Зелен

### 6️⃣ **Автосервиз "Мото Експерт"** (Порт 5010)
```bash
docker run -v ${PWD}/bots/moto_expert_autoservice/rasa:/app -p 5010:5005 rasa/rasa:3.6.15 run --enable-api --cors "*" --port 5005
```
**API:** `http://localhost:5010/webhooks/rest/webhook`
**Web интерфейс:** `http://localhost:5010`
**Цвят:** 🔴 Червен

## 🛠️ Управление

### 📋 **Batch файлове за стартиране:**
- **`start_dragonforged_v2.bat`** - DragonForgedDreams V2 (Порт 5005)
- **`start_zlatna_kosa.bat`** - Салон "Златна коса" (Порт 5006)
- **`start_zlatna_vilitsa.bat`** - Ресторант "Златна вилица" (Порт 5007)
- **`start_grand_sofia.bat`** - Хотел "Гранд София" (Порт 5008)
- **`start_zdrave_medical.bat`** - Медицински център "Здраве+" (Порт 5009)
- **`start_moto_expert.bat`** - Автосервиз "Мото Експерт" (Порт 5010)

### 🎛️ **Управление:**
- **`MULTI_BOT_MENU.bat`** - Главно меню за управление на всички ботове
- **`check_bots_status.bat`** - Проверка на статуса на ботовете
- **`stop_all_bots.bat`** - Спиране на всички ботове
- **`run_tests.bat`** - Стартиране на PowerShell тестове

### 🚀 **Docker Compose (всички ботове едновременно):**
- **`start_all_bots_local.bat`** - Стартиране на всички ботове с Docker Compose
- **`docker-compose-local.yml`** - Конфигурация за всички ботове
- **`nginx-local.conf`** - Nginx конфигурация за локално тестване

## 🌐 Web интерфейси

### 🎨 **Динамични интерфейси:**
- **Автоматично отваряне** в браузъра
- **Проверка на връзката** в реално време
- **Индивидуални цветове** за всеки бот
- **Responsive дизайн** за мобилни устройства

### 📱 **Главна страница:**
- **URL:** `http://localhost:8080` (с Docker Compose)
- **Функции:** Преглед на всички ботове, статус индикатори, бързи линкове

## 🔧 Тестване

### 📊 **PowerShell тестове:**
```powershell
# Стартиране на тестове
.\run_tests.bat

# Ръчно тестване
$body = @{sender="test"; message="здравей"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5005/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

### 🧪 **API тестове:**
- **Health check:** `http://localhost:5005/`
- **Model status:** `http://localhost:5005/model/status`
- **Predict:** `http://localhost:5005/model/predict`

## 📁 Структура на проекта

```
Rasa VPS/
├── bots/
│   ├── dragonforged_bot_v2/
│   │   ├── rasa/           # Rasa конфигурация
│   │   └── web/            # Web интерфейс
│   ├── zlatna_kosa_salon/
│   ├── zlatna_vilitsa_restaurant/
│   ├── grand_sofia_hotel/
│   ├── zdrave_medical_center/
│   └── moto_expert_autoservice/
├── batch файлове/          # Стартиране на ботове
├── docker-compose-local.yml # Docker Compose
├── nginx-local.conf        # Nginx конфигурация
├── index.html              # Главна страница
└── README файлове/         # Документация
```

## 🔄 VPS Deployment

### 🌐 **VPS конфигурация:**
- **IP:** `37.60.225.86`
- **Docker Compose:** `docker-compose-multi.yml`
- **Nginx:** `nginx-multi.conf`
- **Web интерфейси:** Автоматично се адаптират

### 📤 **Качване в VPS:**
```bash
# Копиране на файлове
scp -r ./* root@37.60.225.86:/opt/rasa/

# Стартиране в VPS
docker-compose -f docker-compose-multi.yml up -d
```

## ✅ Проверка на функционалността

### 🔍 **Локално тестване:**
1. Стартирайте бот с batch файл
2. Изчакайте 15-20 секунди
3. Web интерфейсът се отваря автоматично
4. Тествайте чата

### 🌐 **VPS тестване:**
1. Качете файловете в VPS
2. Стартирайте с Docker Compose
3. Отворете `http://37.60.225.86/dragonforged-v2`
4. Тествайте функционалността

## 🎯 Резултат

### ✅ **Локално:**
- **Batch файлове** отварят браузъра автоматично
- **Web интерфейси** използват localhost
- **API endpoints** работят на правилните портове

### ✅ **VPS:**
- **Nginx** проксира заявките
- **Web интерфейси** използват VPS URL-и
- **Всички ботове** работят едновременно

### 🔄 **Автоматично адаптиране:**
- **Един код** работи в двете среди
- **JavaScript** определя средата автоматично
- **Без промени** при качване в VPS

---

**🎉 Системата работи точно както преди - и локално, и в VPS!**
