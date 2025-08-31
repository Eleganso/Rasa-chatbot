#!/usr/bin/env python3
"""
Rasa Bot Development Tool
Easily add new intents to your Rasa bot
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

def add_new_intents():
    """Add new intents to the bot"""
    
    # New intents to add
    new_intents = {
        'weather': {
            'examples': [
                "what's the weather like",
                "how's the weather", 
                "weather forecast",
                "is it raining",
                "temperature today",
                "weather today",
                "what's the temperature",
                "is it sunny",
                "weather report",
                "климатични условия",
                "какво е времето",
                "времето днес",
                "ще вали ли",
                "температурата"
            ]
        },
        'help': {
            'examples': [
                "help",
                "I need help",
                "can you help me",
                "what can you do",
                "how can you help",
                "assistance",
                "support",
                "помощ",
                "нужна ми е помощ",
                "можеш ли да ми помогнеш",
                "какво можеш да правиш"
            ]
        },
        'thanks': {
            'examples': [
                "thanks",
                "thank you",
                "thanks a lot",
                "thank you very much",
                "thanks so much",
                "благодаря",
                "мерси",
                "благодаря ти",
                "много благодаря"
            ]
        },
        'joke': {
            'examples': [
                "tell me a joke",
                "say something funny",
                "make me laugh",
                "joke",
                "funny story",
                "разкажи ми виц",
                "кажи нещо забавно",
                "разсмеши ме",
                "виц"
            ]
        },
        'time': {
            'examples': [
                "what time is it",
                "current time",
                "time now",
                "what's the time",
                "колко е часът",
                "текущо време",
                "сегашно време",
                "часът"
            ]
        },
        'name': {
            'examples': [
                "what's your name",
                "what should I call you",
                "who are you",
                "your name",
                "как се казваш",
                "какво е твоето име",
                "кой си ти",
                "твоето име"
            ]
        },
        'capabilities': {
            'examples': [
                "what can you do",
                "your capabilities",
                "what are your features",
                "what do you do",
                "какво можеш да правиш",
                "твоите възможности",
                "какви са функциите ти",
                "какво правиш"
            ]
        }
    }
    
    # Load current NLU data
    nlu_file = "rasa/data/nlu.yml"
    nlu_data = load_yaml(nlu_file)
    
    if not nlu_data:
        print("❌ Could not load NLU data")
        return False
    
    # Add new intents
    for intent_name, intent_data in new_intents.items():
        new_intent = {
            'intent': intent_name,
            'examples': '|\n    ' + '\n    '.join([f'- {example}' for example in intent_data['examples']])
        }
        nlu_data['nlu'].append(new_intent)
        print(f"✅ Added intent: {intent_name}")
    
    # Save updated NLU data
    save_yaml(nlu_data, nlu_file)
    print("✅ Updated NLU data")
    
    return True

def update_domain():
    """Update domain.yml with new intents and responses"""
    
    # New responses
    new_responses = {
        'utter_weather': [
            "I'm sorry, I can't check the weather right now. But I can tell you a joke to brighten your day!",
            "Съжалявам, не мога да проверя времето сега. Но мога да ти разкажа виц!"
        ],
        'utter_help': [
            "I can help you with:\n- Greetings and conversations\n- Telling jokes\n- Checking the time\n- Answering questions\n- Making you feel better when you're sad",
            "Мога да ти помогна с:\n- Поздравления и разговори\n- Разказване на вицове\n- Проверка на часа\n- Отговаряне на въпроси\n- Да те развеселя когато си тъжен"
        ],
        'utter_thanks': [
            "You're welcome! 😊",
            "Моля! 😊",
            "Радвам се да помогна!"
        ],
        'utter_joke': [
            "Why don't scientists trust atoms? Because they make up everything! 😄",
            "Защо учените не се доверяват на атомите? Защото те съставят всичко! 😄",
            "What do you call a bear with no teeth? A gummy bear! 🐻",
            "Как наричаш мечка без зъби? Желатинена мечка! 🐻"
        ],
        'utter_time': [
            "I can't tell you the exact time, but I can tell you that time is what keeps everything from happening at once! 😉",
            "Не мога да ти кажа точния час, но мога да ти кажа, че времето е това, което не позволява всичко да се случва наведнъж! 😉"
        ],
        'utter_name': [
            "I'm RasaBot, your friendly AI assistant! 🤖",
            "Аз съм RasaBot, твоят приятелски AI асистент! 🤖"
        ],
        'utter_capabilities': [
            "I'm a conversational AI that can:\n- Chat with you\n- Tell jokes\n- Help you feel better\n- Answer questions\n- And much more! What would you like to know?",
            "Аз съм разговорен AI, който може да:\n- Разговаря с теб\n- Разказва вицове\n- Те развесели\n- Отговаря на въпроси\n- И още много! Какво искаш да знаеш?"
        ]
    }
    
    # Load current domain
    domain_file = "rasa/domain.yml"
    domain_data = load_yaml(domain_file)
    
    if not domain_data:
        print("❌ Could not load domain data")
        return False
    
    # Add new intents
    new_intent_names = ['weather', 'help', 'thanks', 'joke', 'time', 'name', 'capabilities']
    for intent_name in new_intent_names:
        if intent_name not in domain_data['intents']:
            domain_data['intents'].append(intent_name)
    
    # Add new responses
    for response_name, response_texts in new_responses.items():
        domain_data['responses'][response_name] = []
        for text in response_texts:
            domain_data['responses'][response_name].append({'text': text})
    
    # Add Bulgarian responses to existing responses
    domain_data['responses']['utter_greet'].extend([
        {'text': 'Здравей! Как си?'},
        {'text': 'Привет! Как върви?'}
    ])
    
    domain_data['responses']['utter_goodbye'].extend([
        {'text': 'Довиждане!'},
        {'text': 'Чао!'}
    ])
    
    # Save updated domain
    save_yaml(domain_data, domain_file)
    print("✅ Updated domain data")
    
    return True

def update_stories():
    """Update stories.yml with new conversation flows"""
    
    # New stories
    new_stories = [
        {
            'story': 'weather inquiry',
            'steps': [
                {'intent': 'weather'},
                {'action': 'utter_weather'}
            ]
        },
        {
            'story': 'help request',
            'steps': [
                {'intent': 'help'},
                {'action': 'utter_help'}
            ]
        },
        {
            'story': 'thanks',
            'steps': [
                {'intent': 'thanks'},
                {'action': 'utter_thanks'}
            ]
        },
        {
            'story': 'joke request',
            'steps': [
                {'intent': 'joke'},
                {'action': 'utter_joke'}
            ]
        },
        {
            'story': 'time inquiry',
            'steps': [
                {'intent': 'time'},
                {'action': 'utter_time'}
            ]
        },
        {
            'story': 'name inquiry',
            'steps': [
                {'intent': 'name'},
                {'action': 'utter_name'}
            ]
        },
        {
            'story': 'capabilities inquiry',
            'steps': [
                {'intent': 'capabilities'},
                {'action': 'utter_capabilities'}
            ]
        }
    ]
    
    # Load current stories
    stories_file = "rasa/data/stories.yml"
    stories_data = load_yaml(stories_file)
    
    if not stories_data:
        print("❌ Could not load stories data")
        return False
    
    # Add new stories
    for story in new_stories:
        stories_data['stories'].append(story)
    
    # Save updated stories
    save_yaml(stories_data, stories_file)
    print("✅ Updated stories data")
    
    return True

def create_development_guide():
    """Create development guide"""
    
    guide_content = """# Rasa Bot Development Guide

## How to Add New Intents

### 1. Add Training Examples
Edit `rasa/data/nlu.yml` and add new intent:

```yaml
- intent: your_new_intent
  examples: |
    - example 1
    - example 2
    - example 3
```

### 2. Add to Domain
Edit `rasa/domain.yml` and add:
- intent name to intents list
- response in responses section

### 3. Add Stories
Edit `rasa/data/stories.yml` and add conversation flow:

```yaml
- story: your story name
  steps:
  - intent: your_new_intent
  - action: utter_your_response
```

### 4. Train the Bot
Run: `docker run --rm -v "%cd%\\rasa:/app" rasa/rasa:3.6.21 train --force`

### 5. Test
Start web chat: `.\start_web_chat.bat`

## New Intents Added:
- **weather**: Ask about weather
- **help**: Get help and capabilities  
- **thanks**: Respond to thanks
- **joke**: Tell jokes
- **time**: Ask about time
- **name**: Ask bot's name
- **capabilities**: Ask what bot can do

## Bilingual Support:
All new intents support both English and Bulgarian!

## Test Examples:
- "What's the weather like?"
- "Tell me a joke"
- "What can you do?"
- "What's your name?"
- "Thanks"
- "Help"
- "Какво е времето?"
- "Разкажи ми виц"
- "Какво можеш да правиш?"
"""
    
    with open('DEVELOPMENT_GUIDE.md', 'w', encoding='utf-8') as f:
        f.write(guide_content)
    
    print("✅ Created development guide")

def main():
    """Main function"""
    print("🚀 Rasa Bot Development Tool")
    print("=" * 40)
    
    # Create backup
    backup_dir = backup_files()
    
    # Add new intents
    if add_new_intents():
        print("✅ Successfully added new intents")
    else:
        print("❌ Failed to add intents")
        return
    
    # Update domain
    if update_domain():
        print("✅ Successfully updated domain")
    else:
        print("❌ Failed to update domain")
        return
    
    # Update stories
    if update_stories():
        print("✅ Successfully updated stories")
    else:
        print("❌ Failed to update stories")
        return
    
    # Create development guide
    create_development_guide()
    
    print("\n🎉 Bot Enhancement Complete!")
    print("=" * 40)
    print("✅ Added 7 new intents:")
    print("   - weather (времето)")
    print("   - help (помощ)")
    print("   - thanks (благодарности)")
    print("   - joke (виц)")
    print("   - time (час)")
    print("   - name (име)")
    print("   - capabilities (възможности)")
    print("\n✅ Bilingual support (English + Bulgarian)")
    print("✅ Enhanced responses with emojis")
    print("✅ New conversation flows")
    print(f"✅ Backup created in: {backup_dir}")
    print("\n📚 Development Guide: DEVELOPMENT_GUIDE.md")
    print("\n🎯 Next steps:")
    print("1. Train the bot: docker run --rm -v \"%cd%\\rasa:/app\" rasa/rasa:3.6.21 train --force")
    print("2. Test: .\\start_web_chat.bat")
    print("3. Try: \"What's the weather like?\", \"Tell me a joke\", \"Help\"")

if __name__ == "__main__":
    main()
