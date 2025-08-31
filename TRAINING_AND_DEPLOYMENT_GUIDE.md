# 🚀 Ръководство за Трениране и Деплойване на Новите Ботове

## 📋 Проблем
Новите 5 ботове използват моделите на DragonForged V2 вместо собствените си модели. Трябва да ги тренираме локално и да качим моделите на VPS.

## 🔧 Стъпки за Решение

### 1️⃣ **Трениране на Ботове Локално**

#### Опция A: Трениране на всички ботове наведнъж
```bash
# Стартирайте Docker Desktop първо!
train_all_new_bots.bat
```

#### Опция B: Трениране на отделни ботове
```bash
# Салон 'Златна коса'
train_zlatna_kosa.bat

# Ресторант 'Златна вилица'
train_zlatna_vilitsa.bat

# Хотел 'Гранд София'
train_grand_sofia.bat

# Медицински център 'Здраве+'
train_zdrave_medical.bat

# Автосервиз 'Мото Експерт'
train_moto_expert.bat
```

### 2️⃣ **Качване на Моделите на VPS**

След успешното трениране, качете моделите на VPS:

```bash
python upload_models_to_vps.py
```

## 📁 Структура на Файловете

### Локални директории за модели:
```
bots/
├── zlatna_kosa_salon/rasa/models/          # Модели за Салон
├── zlatna_vilitsa_restaurant/rasa/models/  # Модели за Ресторант
├── grand_sofia_hotel/rasa/models/          # Модели за Хотел
├── zdrave_medical_center/rasa/models/      # Модели за Медицински център
└── moto_expert_autoservice/rasa/models/    # Модели за Автосервиз
```

### VPS директории за модели:
```
/root/multi-bots/
├── bots/zlatna_kosa_salon/rasa/models/
├── bots/zlatna_vilitsa_restaurant/rasa/models/
├── bots/grand_sofia_hotel/rasa/models/
├── bots/zdrave_medical_center/rasa/models/
└── bots/moto_expert_autoservice/rasa/models/
```

## 🧪 Тестване

### След тренирането локално:
```bash
# Стартиране на бот за тестване
start_zlatna_kosa_salon.bat
start_zlatna_vilitsa_restaurant.bat
start_grand_sofia_hotel.bat
start_zdrave_medical_center.bat
start_moto_expert_autoservice.bat
```

### След качването на VPS:
```
http://37.60.225.86/zlatna-kosa/
http://37.60.225.86/zlatna-vilitsa/
http://37.60.225.86/grand-sofia/
http://37.60.225.86/zdrave-medical/
http://37.60.225.86/moto-expert/
```

## ⚠️ Важни Забележки

1. **Docker Desktop**: Уверете се, че Docker Desktop е стартиран преди тренирането
2. **Време за трениране**: Всяко трениране отнема 2-5 минути
3. **Размер на моделите**: Моделите са около 50-100MB всеки
4. **Съвместимост**: Използваме Rasa 3.6.21 за съвместимост

## 🔄 Процес на Обновяване

За да обновите ботове в бъдеще:

1. **Променете данните** в `data/nlu.yml`, `domain.yml`
2. **Тренирайте локално** с batch файловете
3. **Качете моделите** с `upload_models_to_vps.py`
4. **Рестартирайте контейнерите** на VPS

## 📊 Статус на Ботовете

| Бот | Статус | URL | Модел |
|-----|--------|-----|-------|
| Салон 'Златна коса' | ✅ Работи | http://37.60.225.86/zlatna-kosa/ | Трябва трениране |
| Ресторант 'Златна вилица' | ✅ Работи | http://37.60.225.86/zlatna-vilitsa/ | Трябва трениране |
| Хотел 'Гранд София' | ✅ Работи | http://37.60.225.86/grand-sofia/ | Трябва трениране |
| Медицински център 'Здраве+' | ✅ Работи | http://37.60.225.86/zdrave-medical/ | Трябва трениране |
| Автосервиз 'Мото Експерт' | ✅ Работи | http://37.60.225.86/moto-expert/ | Трябва трениране |

## 🎯 Следващи Стъпки

1. **Стартирайте Docker Desktop**
2. **Изпълнете `train_all_new_bots.bat`**
3. **Изпълнете `python upload_models_to_vps.py`**
4. **Тествайте ботовете**

---

**💡 Съвет**: Ако имате проблеми с Docker, можете да използвате виртуалната среда `rasa_env` за трениране, но Docker е по-надежден за консистентност.
