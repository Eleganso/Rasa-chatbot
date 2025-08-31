# 🔗 БЪРЗИ ЛИНКОВЕ - МУЛТИ-БОТ СИСТЕМА

## 🚀 Стартиране на ботове

### 📋 Batch файлове:
- **`MULTI_BOT_MENU.bat`** - Главно меню за управление на всички ботове
- **`start_dragonforged_v2.bat`** - DragonForgedDreams V2 (Порт 5005)
- **`start_zlatna_kosa.bat`** - Салон "Златна коса" (Порт 5006)
- **`start_zlatna_vilitsa.bat`** - Ресторант "Златна вилица" (Порт 5007)
- **`start_grand_sofia.bat`** - Хотел "Гранд София" (Порт 5008)
- **`start_zdrave_medical.bat`** - Медицински център "Здраве+" (Порт 5009)
- **`start_moto_expert.bat`** - Автосервиз "Мото Експерт" (Порт 5010)

### 🛠️ Управление:
- **`check_bots_status.bat`** - Проверка на статуса на ботовете
- **`stop_all_bots.bat`** - Спиране на всички ботове
- **`run_tests.bat`** - Стартиране на PowerShell тестове

## 🌐 API Endpoints

### Локални URL-и:
| Бот | API Endpoint | Web интерфейс |
|-----|--------------|---------------|
| **DragonForgedDreams V2** | `http://localhost:5005/webhooks/rest/webhook` | `http://localhost:5005` |
| **Салон "Златна коса"** | `http://localhost:5006/webhooks/rest/webhook` | `http://localhost:5006` |
| **Ресторант "Златна вилица"** | `http://localhost:5007/webhooks/rest/webhook` | `http://localhost:5007` |
| **Хотел "Гранд София"** | `http://localhost:5008/webhooks/rest/webhook` | `http://localhost:5008` |
| **Медицински център "Здраве+"** | `http://localhost:5009/webhooks/rest/webhook` | `http://localhost:5009` |
| **Автосервиз "Мото Експерт"** | `http://localhost:5010/webhooks/rest/webhook` | `http://localhost:5010` |

### VPS URL-и:
| Бот | API Endpoint | Web интерфейс |
|-----|--------------|---------------|
| **DragonForgedDreams V2** | `http://37.60.225.86/dragonforged/webhooks/rest/webhook` | `http://37.60.225.86/dragonforged/` |
| **Салон "Златна коса"** | `http://37.60.225.86/zlatna-kosa/webhooks/rest/webhook` | `http://37.60.225.86/zlatna-kosa/` |
| **Ресторант "Златна вилица"** | `http://37.60.225.86/zlatna-vilitsa/webhooks/rest/webhook` | `http://37.60.225.86/zlatna-vilitsa/` |
| **Хотел "Гранд София"** | `http://37.60.225.86/grand-sofia/webhooks/rest/webhook` | `http://37.60.225.86/grand-sofia/` |
| **Медицински център "Здраве+"** | `http://37.60.225.86/zdravet-plus/webhooks/rest/webhook` | `http://37.60.225.86/zdravet-plus/` |
| **Автосервиз "Мото Експерт"** | `http://37.60.225.86/moto-expert/webhooks/rest/webhook` | `http://37.60.225.86/moto-expert/` |

## 🧪 Тестване

### PowerShell команда за тестване:
```powershell
$body = @{sender="test"; message="здравей"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:ПОРТ/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

### Примери за тестване:

#### DragonForgedDreams V2:
```powershell
$body = @{sender="test"; message="какви услуги предлагате"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5005/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

#### Салон "Златна коса":
```powershell
$body = @{sender="test"; message="имате ли свободно време за подстригване"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5006/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

#### Ресторант "Златна вилица":
```powershell
$body = @{sender="test"; message="какво има в менюто"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5007/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

#### Хотел "Гранд София":
```powershell
$body = @{sender="test"; message="имате ли свободни стаи"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5008/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

#### Медицински център "Здраве+":
```powershell
$body = @{sender="test"; message="кога мога да се запиша за преглед"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5009/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

#### Автосервиз "Мото Експерт":
```powershell
$body = @{sender="test"; message="имате ли свободно време за ремонт"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://localhost:5010/webhooks/rest/webhook" -Method POST -ContentType "application/json" -Body $body
```

## 📚 Документация

- **`README_MULTI_BOT_LOCAL_TEST.md`** - Подробно ръководство за локално тестване
- **`MULTI_BOT_SYSTEM_GUIDE.md`** - Общо ръководство за мулти-бот системата
- **`BOT_PORTS_INFO.md`** - Информация за портове и конфигурация

## 🐳 Docker команди

### Проверка на статуса:
```bash
docker ps
```

### Спиране на всички контейнери:
```bash
docker stop $(docker ps -q)
```

### Проверка на логове:
```bash
docker logs КОНТЕЙНЕР_ID
```

## ⚡ Бърз старт

1. **Стартирайте главното меню:** `MULTI_BOT_MENU.bat`
2. **Изберете бот** за стартиране
3. **Изчакайте** 15-20 секунди за зареждане
4. **Тествайте** с `run_tests.bat` или PowerShell командите
5. **Спрете бота** преди да стартирате друг

---

**🎉 Всички линкове са готови за използване!** 🚀

*Последна актуализация: 31.08.2025*
