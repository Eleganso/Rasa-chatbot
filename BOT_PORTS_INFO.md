# 📋 Информация за портовете на ботовете

## 🐳 Docker контейнери и портове

### 🚀 Активни ботове (6 общо):

| № | Бот | Контейнер име | Външен порт | Вътрешен порт | URL |
|---|-----|---------------|-------------|---------------|-----|
| 1 | **DragonForged Dreams V2** | `dragonforged_v2` | **5005** | 5005 | http://37.60.225.86/dragonforged/ |
| 2 | **Салон "Златна коса"** | `zlatna_kosa` | **5006** | 5005 | http://37.60.225.86/zlatna-kosa/ |
| 3 | **Ресторант "Златна вилица"** | `zlatna_vilitsa` | **5007** | 5005 | http://37.60.225.86/zlatna-vilitsa/ |
| 4 | **Хотел "Гранд София"** | `grand_sofia` | **5008** | 5005 | http://37.60.225.86/grand-sofia/ |
| 5 | **Медицински център "Здраве+"** | `zdravet_plus` | **5009** | 5005 | http://37.60.225.86/zdravet-plus/ |
| 6 | **Автосервиз "Мото Експерт"** | `moto_expert` | **5010** | 5005 | http://37.60.225.86/moto-expert/ |

### 🌐 Nginx Reverse Proxy:
- **Контейнер:** `multi-bot-nginx`
- **HTTP порт:** **80**
- **HTTPS порт:** **443** (готов за SSL)

## 🔧 Технически детайли:

### 📁 Директории на VPS:
```
/root/multi-bots/
├── docker-compose.yml
├── nginx.conf
└── bots/
    ├── dragonforged_bot_v2/
    ├── zlatna_kosa_salon/
    ├── zlatna_vilitsa_restaurant/
    ├── grand_sofia_hotel/
    ├── zdravet_plus_medical/
    └── moto_expert_auto/
```

### 🐳 Docker команди:
```bash
# Проверка на статуса
docker-compose ps

# Логове на конкретен бот
docker-compose logs dragonforged_v2

# Рестартиране на бот
docker-compose restart dragonforged_v2

# Рестартиране на всички
docker-compose restart
```

### 🌐 API endpoints:
- **DragonForged:** `http://37.60.225.86/dragonforged/webhooks/rest/webhook`
- **Златна коса:** `http://37.60.225.86/zlatna-kosa/webhooks/rest/webhook`
- **Златна вилица:** `http://37.60.225.86/zlatna-vilitsa/webhooks/rest/webhook`
- **Гранд София:** `http://37.60.225.86/grand-sofia/webhooks/rest/webhook`
- **Здраве+:** `http://37.60.225.86/zdravet-plus/webhooks/rest/webhook`
- **Мото Експерт:** `http://37.60.225.86/moto-expert/webhooks/rest/webhook`

## 📊 Статус на ресурсите:
- **RAM използване:** ~2.2GB от 11GB (20%)
- **CPU натоварване:** Минимално
- **Дисково пространство:** 5.8GB от 96GB (6%)

## ✅ Всички ботове работят стабилно!

---
*Последна актуализация: 31.08.2025*
