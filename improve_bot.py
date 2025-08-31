#!/usr/bin/env python3
"""
Improve Rasa Bot with more Bulgarian examples and proper model
"""

import os
import yaml
import shutil
from datetime import datetime

def backup_files():
    """Create backup of current files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"backup_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    
    files_to_backup = [
        "rasa/data/nlu.yml",
        "rasa/domain.yml", 
        "rasa/data/stories.yml"
    ]
    
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            shutil.copy2(file_path, backup_dir)
    
    print(f"✅ Backup created in: {backup_dir}")
    return backup_dir

def load_yaml(file_path):
    """Load YAML file"""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    return None

def save_yaml(data, file_path):
    """Save data to YAML file"""
    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

def improve_nlu_data():
    """Improve NLU data with more Bulgarian examples"""
    
    # Load current NLU data
    nlu_file = "rasa/data/nlu.yml"
    nlu_data = load_yaml(nlu_file)
    
    if not nlu_data:
        print("❌ Could not load NLU data")
        return False
    
    # Find and improve existing intents
    for intent in nlu_data['nlu']:
        if intent['intent'] == 'greet':
            # Add more Bulgarian greetings
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - здрасти",
                "    - здравей",
                "    - привет",
                "    - добър ден",
                "    - добро утро",
                "    - добър вечер",
                "    - здраве",
                "    - здравеи",
                "    - здрастики",
                "    - здравейте",
                "    - привети",
                "    - чао",
                "    - хей",
                "    - хело",
                "    - хай",
                "    - ало",
                "    - алоо",
                "    - алоу"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced greet intent with Bulgarian examples")
            
        elif intent['intent'] == 'goodbye':
            # Add more Bulgarian goodbyes
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - довиждане",
                "    - чао",
                "    - довиждане",
                "    - приятен ден",
                "    - лека вечер",
                "    - лека нощ",
                "    - до скоро",
                "    - до следващо",
                "    - до утре",
                "    - до видене",
                "    - приятно",
                "    - успех",
                "    - мерси",
                "    - благодаря",
                "    - мерси много"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced goodbye intent with Bulgarian examples")
            
        elif intent['intent'] == 'weather':
            # Add more Bulgarian weather examples
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - какво е времето",
                "    - времето какво е",
                "    - ще вали ли",
                "    - ще е слънчево ли",
                "    - температурата каква е",
                "    - градусите колко са",
                "    - времето днес",
                "    - времето утре",
                "    - климатични условия",
                "    - метео",
                "    - прогноза за времето",
                "    - времето в София",
                "    - времето в България",
                "    - ще е студено ли",
                "    - ще е топло ли"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced weather intent with Bulgarian examples")
            
        elif intent['intent'] == 'joke':
            # Add more Bulgarian joke examples
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - разкажи ми виц",
                "    - кажи виц",
                "    - разкажи виц",
                "    - кажи нещо забавно",
                "    - разсмеши ме",
                "    - забавлявай ме",
                "    - кажи нещо смешно",
                "    - разкажи нещо забавно",
                "    - виц",
                "    - вицче",
                "    - шега",
                "    - шегичка",
                "    - забавна история",
                "    - смешна история",
                "    - анекдот"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced joke intent with Bulgarian examples")
            
        elif intent['intent'] == 'help':
            # Add more Bulgarian help examples
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - помощ",
                "    - нужна ми е помощ",
                "    - можеш ли да ми помогнеш",
                "    - какво можеш да правиш",
                "    - какво умееш",
                "    - какво знаеш",
                "    - какво можеш",
                "    - какво си способен",
                "    - какви са възможностите ти",
                "    - какви са функциите ти",
                "    - какво правиш",
                "    - какво си",
                "    - какво си ти",
                "    - какво си за бот",
                "    - какво си за асистент"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced help intent with Bulgarian examples")
            
        elif intent['intent'] == 'thanks':
            # Add more Bulgarian thanks examples
            current_examples = intent['examples'].split('\n')
            new_examples = [
                "    - благодаря",
                "    - мерси",
                "    - благодаря ти",
                "    - много благодаря",
                "    - мерси много",
                "    - благодаря много",
                "    - благодаря ти много",
                "    - мерси ти",
                "    - благодаря ти много",
                "    - много мерси",
                "    - благодаря ти много",
                "    - мерси ти много",
                "    - благодаря ти много",
                "    - мерси ти много",
                "    - благодаря ти много"
            ]
            intent['examples'] = intent['examples'].rstrip() + '\n' + '\n'.join(new_examples)
            print("✅ Enhanced thanks intent with Bulgarian examples")
    
    # Save updated NLU data
    save_yaml(nlu_data, nlu_file)
    print("✅ Updated NLU data with more Bulgarian examples")
    
    return True

def improve_domain():
    """Improve domain with better responses and bot name"""
    
    # Load current domain
    domain_file = "rasa/domain.yml"
    domain_data = load_yaml(domain_file)
    
    if not domain_data:
        print("❌ Could not load domain data")
        return False
    
    # Improve existing responses
    domain_data['responses']['utter_greet'] = [
        {'text': "Здравей! Аз съм SofiaBot, твоят български AI асистент! 🤖 Как мога да ти помогна?"},
        {'text': "Привет! Казвам се SofiaBot и съм тук да ти помогна! 😊 Какво искаш да знаеш?"},
        {'text': "Здрасти! Аз съм SofiaBot - твоят приятелски български бот! 🎉 Как си?"},
        {'text': "Добър ден! SofiaBot на ваше разположение! 🤖 Как мога да ви помогна?"},
        {'text': "Здравейте! Аз съм SofiaBot, вашият AI асистент! 😊 Какво искате да знаете?"}
    ]
    
    domain_data['responses']['utter_goodbye'] = [
        {'text': "Довиждане! Радвам се, че успях да помогна! 😊"},
        {'text': "Чао! Надявам се да сме се виждали отново скоро! 👋"},
        {'text': "Довиждане! SofiaBot винаги е тук за вас! 🤖"},
        {'text': "Приятен ден! SofiaBot се прощава! 😄"},
        {'text': "До скоро! SofiaBot винаги е готов да помогне! 🎉"}
    ]
    
    domain_data['responses']['utter_name'] = [
        {'text': "Аз съм SofiaBot! 🤖 Твоят български AI асистент, който винаги е готов да помогне!"},
        {'text': "Казвам се SofiaBot! 😊 Аз съм тук да ти помогна с всичко, което искаш!"},
        {'text': "SofiaBot е името ми! 🎉 Твоят приятелски български бот!"},
        {'text': "SofiaBot съм! 🤖 Вашият AI асистент, който говори български!"},
        {'text': "SofiaBot! 😊 Твоят български помощник в дигиталния свят!"}
    ]
    
    domain_data['responses']['utter_capabilities'] = [
        {'text': "SofiaBot може да:\n- Разговаря на български и английски\n- Разказва вицове и забавни истории\n- Отговаря на въпроси за времето\n- Помога с различни задачи\n- Те развесели когато си тъжен\n- И още много! 🤖\n\nКакво искаш да знаеш?"},
        {'text': "Като SofiaBot мога да:\n- Говоря на български перфектно\n- Разказвам вицове и шеги\n- Отговарям на въпроси\n- Те развеселя\n- Помогам с информация\n- Бъда твоят приятелски асистент! 😊\n\nКакво те интересува?"},
        {'text': "SofiaBot е твоят български AI асистент, който може да:\n- Разговаря естествено на български\n- Разказва забавни истории\n- Отговаря на въпроси\n- Помога с различни задачи\n- Те развесели\n- Бъде твоят дигитален приятел! 🎉\n\nКакво искаш да знаеш?"}
    ]
    
    domain_data['responses']['utter_joke'] = [
        {'text': "Ето един български виц:\n\nЗащо българинът носи две часовника?\nЗащото единият показва времето, а другият - колко време му остава! 😄"},
        {'text': "Защо учените не се доверяват на атомите?\nЗащото те съставят всичко! 😄\n\nА ето и един български:\nКак наричаш мечка без зъби?\nЖелатинена мечка! 🐻"},
        {'text': "Ето един забавен виц:\n\nЗащо програмистът отиде в магазина?\nЗащото му трябваше хляб... и мляко... и яйца... и масло... и сирене... 😂\n\nSofiaBot винаги е готов да те разсмее! 🎉"}
    ]
    
    domain_data['responses']['utter_weather'] = [
        {'text': "Съжалявам, SofiaBot не може да проверя времето в реално време, но мога да ти разкажа виц за да те развеселя! 😄"},
        {'text': "SofiaBot все още не може да проверя времето, но мога да ти разкажа забавна история вместо това! 🎉"},
        {'text': "За времето най-добре провери в интернет, но SofiaBot може да те развесели с виц! 😊"}
    ]
    
    domain_data['responses']['utter_help'] = [
        {'text': "SofiaBot може да ти помогне с:\n- Разговори на български и английски\n- Разказване на вицове и шеги\n- Отговаряне на въпроси\n- Развеселяване когато си тъжен\n- Бъдане твоят дигитален приятел\n- И още много! 🤖\n\nПросто ми кажи какво искаш!"},
        {'text': "Като SofiaBot мога да:\n- Говоря перфектно български\n- Разказвам забавни истории\n- Отговарям на въпроси\n- Те развеселя\n- Бъда твоят AI приятел\n- Помогам с информация\n\nКакво те интересува? 😊"}
    ]
    
    domain_data['responses']['utter_thanks'] = [
        {'text': "Моля! SofiaBot винаги е готов да помогне! 😊"},
        {'text': "Радвам се, че успях да помогна! SofiaBot е тук за вас! 🤖"},
        {'text': "Моля! За SofiaBot е удоволствие да помага! 🎉"},
        {'text': "Няма защо! SofiaBot е тук да служи! 😄"},
        {'text': "Моля! Радвам се, че успях да помогна! SofiaBot винаги е готов! 🤖"}
    ]
    
    # Save updated domain
    save_yaml(domain_data, domain_file)
    print("✅ Updated domain with SofiaBot personality and better responses")
    
    return True

def update_start_script():
    """Update start script to use the latest model"""
    
    # Find the latest model
    models_dir = "rasa/models"
    if os.path.exists(models_dir):
        model_files = [f for f in os.listdir(models_dir) if f.endswith('.tar.gz')]
        if model_files:
            # Sort by modification time to get the latest
            model_files.sort(key=lambda x: os.path.getmtime(os.path.join(models_dir, x)), reverse=True)
            latest_model = model_files[0]
            print(f"✅ Latest model found: {latest_model}")
            
            # Update start script
            start_script_content = f"""@echo off
echo =========================================
echo    Starting SofiaBot - Web Chat Interface
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Starting SofiaBot server...
echo Starting SofiaBot server in background...
start "SofiaBot Server" cmd /k "docker run --rm -v "%cd%\rasa:/app" -p 5005:5005 rasa/rasa:3.6.21 run --enable-api --cors "*" --port 5005 --model models/{latest_model}"

echo.
echo Waiting for SofiaBot to start...
timeout /t 20 /nobreak >nul

echo.
echo Step 3: Opening SofiaBot chat interface...
start "" "web_chat\index.html"

echo.
echo =========================================
echo    SofiaBot Ready!
echo =========================================
echo.
echo ✅ SofiaBot server is running on http://localhost:5005
echo ✅ SofiaBot chat interface opened in your browser
echo ✅ SofiaBot is ready to chat in Bulgarian!
echo.
echo SofiaBot features:
echo - Говори перфектно български
echo - Разказва вицове и шеги
echo - Помога с въпроси
echo - Развеселява когато си тъжен
echo.
echo Chat interface location:
echo   web_chat\index.html
echo.
echo Enjoy chatting with SofiaBot! 🎉
echo.
pause"""
            
            with open('start_sofia_bot.bat', 'w', encoding='utf-8') as f:
                f.write(start_script_content)
            
            print("✅ Created start_sofia_bot.bat with latest model")
            return True
    
    print("❌ No models found")
    return False

def main():
    """Main function"""
    print("🚀 SofiaBot Improvement Tool")
    print("=" * 40)
    
    # Create backup
    backup_dir = backup_files()
    
    # Improve NLU data
    if improve_nlu_data():
        print("✅ Successfully improved NLU data")
    else:
        print("❌ Failed to improve NLU data")
        return
    
    # Improve domain
    if improve_domain():
        print("✅ Successfully improved domain")
    else:
        print("❌ Failed to improve domain")
        return
    
    # Update start script
    if update_start_script():
        print("✅ Successfully updated start script")
    else:
        print("❌ Failed to update start script")
        return
    
    print("\n🎉 SofiaBot Improvement Complete!")
    print("=" * 40)
    print("✅ Enhanced with more Bulgarian examples")
    print("✅ SofiaBot personality added")
    print("✅ Better responses in Bulgarian")
    print("✅ Latest model will be used")
    print(f"✅ Backup created in: {backup_dir}")
    print("\n🎯 Next steps:")
    print("1. Train SofiaBot: docker run --rm -v \"%cd%\\rasa:/app\" rasa/rasa:3.6.21 train --force")
    print("2. Start SofiaBot: .\\start_sofia_bot.bat")
    print("3. Test: \"Здрасти\", \"Какво можеш да правиш?\", \"Разкажи ми виц\"")

if __name__ == "__main__":
    main()
