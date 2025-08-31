@echo off
echo =========================================
echo    Rasa Bot Development Tool
echo =========================================
echo.

echo Step 1: Adding Docker to PATH...
set PATH=%PATH%;C:\Program Files\Docker\Docker\resources\bin

echo.
echo Step 2: Creating enhanced bot with new intents...
echo.

echo Step 3: Adding new intents to NLU data...
(
echo # Adding new intents to existing nlu.yml
echo.
echo - intent: weather
echo   examples: |
echo     - what's the weather like
echo     - how's the weather
echo     - weather forecast
echo     - is it raining
echo     - temperature today
echo     - weather today
echo     - what's the temperature
echo     - is it sunny
echo     - weather report
echo     - климатични условия
echo     - какво е времето
echo     - времето днес
echo     - ще вали ли
echo     - температурата
echo.
echo - intent: help
echo   examples: |
echo     - help
echo     - I need help
echo     - can you help me
echo     - what can you do
echo     - how can you help
echo     - assistance
echo     - support
echo     - помощ
echo     - нужна ми е помощ
echo     - можеш ли да ми помогнеш
echo     - какво можеш да правиш
echo.
echo - intent: thanks
echo   examples: |
echo     - thanks
echo     - thank you
echo     - thanks a lot
echo     - thank you very much
echo     - thanks so much
echo     - благодаря
echo     - мерси
echo     - благодаря ти
echo     - много благодаря
echo.
echo - intent: joke
echo   examples: |
echo     - tell me a joke
echo     - say something funny
echo     - make me laugh
echo     - joke
echo     - funny story
echo     - разкажи ми виц
echo     - кажи нещо забавно
echo     - разсмеши ме
echo     - виц
echo.
echo - intent: time
echo   examples: |
echo     - what time is it
echo     - current time
echo     - time now
echo     - what's the time
echo     - колко е часът
echo     - текущо време
echo     - сегашно време
echo     - часът
echo.
echo - intent: name
echo   examples: |
echo     - what's your name
echo     - what should I call you
echo     - who are you
echo     - your name
echo     - как се казваш
echo     - какво е твоето име
echo     - кой си ти
echo     - твоето име
echo.
echo - intent: capabilities
echo   examples: |
echo     - what can you do
echo     - your capabilities
echo     - what are your features
echo     - what do you do
echo     - какво можеш да правиш
echo     - твоите възможности
echo     - какви са функциите ти
echo     - какво правиш
) > rasa\data\new_intents.yml

echo.
echo Step 4: Creating enhanced domain.yml...
(
echo version: "3.1"
echo.
echo intents:
echo   - greet
echo   - goodbye
echo   - affirm
echo   - deny
echo   - mood_great
echo   - mood_unhappy
echo   - bot_challenge
echo   - weather
echo   - help
echo   - thanks
echo   - joke
echo   - time
echo   - name
echo   - capabilities
echo.
echo entities:
echo   - name
echo   - location
echo.
echo slots:
echo   name:
echo     type: text
echo     mappings:
echo     - type: from_entity
echo       entity: name
echo   location:
echo     type: text
echo     mappings:
echo     - type: from_entity
echo       entity: location
echo.
echo responses:
echo   utter_greet:
echo   - text: "Hey! How are you?"
echo   - text: "Hello! How are you doing?"
echo   - text: "Hi there! How are you?"
echo   - text: "Здравей! Как си?"
echo   - text: "Привет! Как върви?"
echo.
echo   utter_cheer_up:
echo   - text: "Here is something to cheer you up:"
echo     image: "https://i.imgur.com/nGF1K8f.jpg"
echo   - text: "I hope this helps you feel better!"
echo   - text: "Ето нещо, което ще те развесели!"
echo.
echo   utter_did_that_help:
echo   - text: "Did that help you?"
echo   - text: "Did that make you feel better?"
echo   - text: "Помогна ли ти това?"
echo.
echo   utter_happy:
echo   - text: "Great, carry on!"
echo   - text: "Excellent! Keep it up!"
echo   - text: "Страхотно, продължавай!"
echo.
echo   utter_goodbye:
echo   - text: "Bye"
echo   - text: "Goodbye!"
echo   - text: "See you around!"
echo   - text: "Bye bye!"
echo   - text: "Довиждане!"
echo   - text: "Чао!"
echo.
echo   utter_iamabot:
echo   - text: "I am a bot, powered by Rasa."
echo   - text: "Аз съм бот, задвижен от Rasa."
echo.
echo   utter_weather:
echo   - text: "I'm sorry, I can't check the weather right now. But I can tell you a joke to brighten your day!"
echo   - text: "Съжалявам, не мога да проверя времето сега. Но мога да ти разкажа виц!"
echo.
echo   utter_help:
echo   - text: "I can help you with: ^n- Greetings and conversations ^n- Telling jokes ^n- Checking the time ^n- Answering questions ^n- Making you feel better when you're sad"
echo   - text: "Мога да ти помогна с: ^n- Поздравления и разговори ^n- Разказване на вицове ^n- Проверка на часа ^n- Отговаряне на въпроси ^n- Да те развеселя когато си тъжен"
echo.
echo   utter_thanks:
echo   - text: "You're welcome! 😊"
echo   - text: "Моля! 😊"
echo   - text: "Радвам се да помогна!"
echo.
echo   utter_joke:
echo   - text: "Why don't scientists trust atoms? Because they make up everything! 😄"
echo   - text: "Защо учените не се доверяват на атомите? Защото те съставят всичко! 😄"
echo   - text: "What do you call a bear with no teeth? A gummy bear! 🐻"
echo   - text: "Как наричаш мечка без зъби? Желатинена мечка! 🐻"
echo.
echo   utter_time:
echo   - text: "I can't tell you the exact time, but I can tell you that time is what keeps everything from happening at once! 😉"
echo   - text: "Не мога да ти кажа точния час, но мога да ти кажа, че времето е това, което не позволява всичко да се случва наведнъж! 😉"
echo.
echo   utter_name:
echo   - text: "I'm RasaBot, your friendly AI assistant! 🤖"
echo   - text: "Аз съм RasaBot, твоят приятелски AI асистент! 🤖"
echo.
echo   utter_capabilities:
echo   - text: "I'm a conversational AI that can: ^n- Chat with you ^n- Tell jokes ^n- Help you feel better ^n- Answer questions ^n- And much more! What would you like to know?"
echo   - text: "Аз съм разговорен AI, който може да: ^n- Разговаря с теб ^n- Разказва вицове ^n- Те развесели ^n- Отговаря на въпроси ^n- И още много! Какво искаш да знаеш?"
echo.
echo session_config:
echo   session_expiration_time: 60
echo   carry_over_slots_to_new_session: true
) > rasa\domain_enhanced.yml

echo.
echo Step 5: Creating enhanced stories...
(
echo version: "3.1"
echo.
echo stories:
echo - story: happy path
echo   steps:
echo   - intent: greet
echo   - action: utter_greet
echo   - intent: mood_great
echo   - action: utter_happy
echo.
echo - story: sad path 1
echo   steps:
echo   - intent: greet
echo   - action: utter_greet
echo   - intent: mood_unhappy
echo   - action: utter_cheer_up
echo   - action: utter_did_that_help
echo   - intent: affirm
echo   - action: utter_happy
echo.
echo - story: sad path 2
echo   steps:
echo   - intent: greet
echo   - action: utter_greet
echo   - intent: mood_unhappy
echo   - action: utter_cheer_up
echo   - action: utter_did_that_help
echo   - intent: deny
echo   - action: utter_goodbye
echo.
echo - story: say goodbye
echo   steps:
echo   - intent: goodbye
echo   - action: utter_goodbye
echo.
echo - story: bot challenge
echo   steps:
echo   - intent: bot_challenge
echo   - action: utter_iamabot
echo.
echo - story: weather inquiry
echo   steps:
echo   - intent: weather
echo   - action: utter_weather
echo.
echo - story: help request
echo   steps:
echo   - intent: help
echo   - action: utter_help
echo.
echo - story: thanks
echo   steps:
echo   - intent: thanks
echo   - action: utter_thanks
echo.
echo - story: joke request
echo   steps:
echo   - intent: joke
echo   - action: utter_joke
echo.
echo - story: time inquiry
echo   steps:
echo   - intent: time
echo   - action: utter_time
echo.
echo - story: name inquiry
echo   steps:
echo   - intent: name
echo   - action: utter_name
echo.
echo - story: capabilities inquiry
echo   steps:
echo   - intent: capabilities
echo   - action: utter_capabilities
echo.
echo - story: weather then joke
echo   steps:
echo   - intent: weather
echo   - action: utter_weather
echo   - intent: joke
echo   - action: utter_joke
echo.
echo - story: help then thanks
echo   steps:
echo   - intent: help
echo   - action: utter_help
echo   - intent: thanks
echo   - action: utter_thanks
) > rasa\data\stories_enhanced.yml

echo.
echo Step 6: Creating training script...
(
echo @echo off
echo echo Training enhanced Rasa bot...
echo docker run --rm -v "%cd%\rasa:/app" rasa/rasa:3.6.21 train --force
echo echo Training complete!
echo pause
) > train_enhanced.bat

echo.
echo Step 7: Creating development guide...
(
echo # Rasa Bot Development Guide
echo.
echo ## How to Add New Intents
echo.
echo ### 1. Add Training Examples
echo Edit rasa/data/nlu.yml and add new intent:
echo.
echo ```yaml
echo - intent: your_new_intent
echo   examples: |
echo     - example 1
echo     - example 2
echo     - example 3
echo ```
echo.
echo ### 2. Add to Domain
echo Edit rasa/domain.yml and add:
echo - intent name to intents list
echo - response in responses section
echo.
echo ### 3. Add Stories
echo Edit rasa/data/stories.yml and add conversation flow:
echo.
echo ```yaml
echo - story: your story name
echo   steps:
echo   - intent: your_new_intent
echo   - action: utter_your_response
echo ```
echo.
echo ### 4. Train the Bot
echo Run: .\train_enhanced.bat
echo.
echo ### 5. Test
echo Start web chat: .\start_web_chat.bat
echo.
echo ## New Intents Added:
echo - weather: Ask about weather
echo - help: Get help and capabilities
echo - thanks: Respond to thanks
echo - joke: Tell jokes
echo - time: Ask about time
echo - name: Ask bot's name
echo - capabilities: Ask what bot can do
echo.
echo ## Bilingual Support:
echo All new intents support both English and Bulgarian!
) > DEVELOPMENT_GUIDE.md

echo.
echo Step 8: Merging new intents with existing data...
copy rasa\data\nlu.yml rasa\data\nlu_backup.yml
type rasa\data\nlu.yml rasa\data\new_intents.yml > rasa\data\nlu_enhanced.yml
copy rasa\data\nlu_enhanced.yml rasa\data\nlu.yml

echo.
echo Step 9: Updating domain and stories...
copy rasa\domain_enhanced.yml rasa\domain.yml
copy rasa\data\stories_enhanced.yml rasa\data\stories.yml

echo.
echo Step 10: Training the enhanced bot...
echo Training enhanced bot with new intents...
docker run --rm -v "%cd%\rasa:/app" rasa/rasa:3.6.21 train --force

echo.
echo =========================================
echo    Enhanced Bot Development Complete!
echo =========================================
echo.
echo ✅ Added 7 new intents:
echo    - weather (времето)
echo    - help (помощ)
echo    - thanks (благодарности)
echo    - joke (виц)
echo    - time (час)
echo    - name (име)
echo    - capabilities (възможности)
echo.
echo ✅ Bilingual support (English + Bulgarian)
echo ✅ Enhanced responses with emojis
echo ✅ New conversation flows
echo ✅ Backup files created
echo.
echo 📚 Development Guide: DEVELOPMENT_GUIDE.md
echo 🚀 Train again: .\train_enhanced.bat
echo 💬 Test: .\start_web_chat.bat
echo.
echo 🎯 Test the new intents:
echo    - "What's the weather like?"
echo    - "Tell me a joke"
echo    - "What can you do?"
echo    - "What's your name?"
echo    - "Thanks"
echo    - "Help"
echo.
echo Enjoy your enhanced bot! 🎉
echo.
pause
