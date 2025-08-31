#!/usr/bin/env python3
"""
DragonForgedDreams Bot - Version 2
Based on second data source
"""

import os
import yaml

def create_dragonforged_bot_v2():
    """Create DragonForgedDreams bot version 2"""
    
    # Create bot directory
    bot_dir = "bots/dragonforged_bot_v2"
    os.makedirs(f"{bot_dir}/rasa/data", exist_ok=True)
    os.makedirs(f"{bot_dir}/rasa/models", exist_ok=True)
    
    # Create domain.yml
    domain_content = """version: "3.1"

intents:
  - greet
  - goodbye
  - ask_services
  - ask_pricing
  - ask_qr_menu
  - ask_chatbots
  - ask_website
  - ask_seo
  - ask_telegram_bots
  - ask_pwa
  - ask_consultation
  - ask_support
  - ask_contact

entities:
  - service_type
  - price_range
  - business_type
  - platform

slots:
  service_type:
    type: text
    mappings:
    - type: from_entity
      entity: service_type
  price_range:
    type: text
    mappings:
    - type: from_entity
      entity: price_range
  business_type:
    type: text
    mappings:
    - type: from_entity
      entity: business_type
  platform:
    type: text
    mappings:
    - type: from_entity
      entity: platform

responses:
  utter_greet:
  - text: "Здравейте! Добре дошли в DragonForged Dreams! Как мога да ви помогна днес?"
  - text: "Привет! Аз съм виртуалният ви асистент. Какво ви интересува от нашите услуги?"
  - text: "Добър ден! Готов съм да отговоря на въпросите ви за нашите дигитални решения!"

  utter_goodbye:
  - text: "Благодаря за интереса! Очакваме скоро да работим заедно. Приятен ден!"
  - text: "До скоро! Не забравяйте - безплатната консултация ви чака на dragonforgeddreams.com!"
  - text: "Чао! При нужда от дигитални решения, знаете къде да ни намерите!"

  utter_services:
  - text: "Предлагаме: ✅ QR меню хостинг ✅ Чатботове за сайтове и социални мрежи ✅ Telegram ботове за автоматизация ✅ Уебсайт разработка ✅ SEO оптимизация ✅ PWA приложения ✅ Безплатна консултация"
  - text: "DragonForged Dreams се специализира в дигитални решения - от QR менюта до чатботове, уебсайтове и автоматизация на бизнес процеси."
  - text: "Нашите основни услуги включват създаване на чатботове, QR меню системи, уебсайтове, SEO и бизнес автоматизация."

  utter_pricing:
  - text: "За подробни цени посетете нашата pricing страница: dragonforgeddreams.com/pricing или се свържете с нас за персонализирана оферта!"
  - text: "Имаме различни пакети според вашите нужди. За точни цени и сравнение посетете: dragonforgeddreams.com/pricing"
  - text: "Цените варират според услугата - от 4,99 лв/месец за QR меню до индивидуални оферти. Вижте пълната информация на dragonforgeddreams.com/pricing"

  utter_qr_menu:
  - text: "QR Menu услугата ни позволява на ресторанти и заведения да създават дигитални менюта достъпни чрез QR код. Имаме 3 пакета: Стартов (4,99 лв/месец), Професионален (19,99 лв/месец) и Signature (39,99 лв/месец)."
  - text: "Създаваме модерни QR менюта за ресторанти с персонализация, аналитика и мобилна оптимизация. За повече детайли: dragonforgeddreams.com/pricing"

  utter_chatbots:
  - text: "Създаваме интелигентни чатботове за вашия сайт и социални мрежи, които отговарят на клиенти 24/7 и увеличават продажбите."
  - text: "Нашите чатботове помагат за автоматизиране на клиентското обслужване и генериране на повече leads за вашия бизнес."

  utter_website:
  - text: "Разработваме модерни, бързи и SEO-оптимизирани уебсайтове за всякакъв тип бизнес. Цена: от 400 лв за проект."
  - text: "Създаваме професионални уебсайтове с фокус върху потребителското изживяване и конверсии."

  utter_seo:
  - text: "SEO оптимизацията ни помага на вашия сайт да се класира по-високо в Google и да привлича повече органичен трафик и клиенти."
  - text: "Предлагаме цялостна SEO стратегия - от техническа оптимизация до създаване на съдържание и link building."

  utter_telegram_bots:
  - text: "Telegram ботовете ни автоматизират работни процеси, интегрират се с вашите системи и спестяват време на екипа ви."
  - text: "Създаваме персонализирани Telegram ботове за автоматизация на задачи, уведомления и бизнес интеграции."

  utter_pwa:
  - text: "PWA (Progressive Web Apps) са модерни уеб приложения, които работят като мобилни апликации, но не изискват инсталиране от store."
  - text: "Progressive Web Apps комбинират най-доброто от уебсайтовете и мобилните приложения - бързи, надеждни и с офлайн достъп."

  utter_consultation:
  - text: "Предлагаме БЕЗПЛАТНА консултация за вашия проект! Свържете се с нас за персонализирани препоръки и стратегия."
  - text: "Нашата безплатна консултация ще ви помогне да изберете най-подходящите дигитални решения за вашия бизнес."

  utter_support:
  - text: "Предлагаме професионална техническа поддръжка за 50 лв/месец, включваща консултации и решаване на проблеми."
  - text: "Нашият support екип е готов да ви помогне с всякакви технически въпроси и актуализации на проектите ви."

  utter_contact:
  - text: "Свържете се с нас чрез сайта dragonforgeddreams.com или заявете безплатна консултация директно оттам!"
  - text: "За контакт използвайте формата на нашия сайт dragonforgeddreams.com - ще се свържем с вас максимално бързо!"

session_config:
  session_expiration_time: 60
  carry_over_slots_to_new_session: true
"""
    
    with open(f"{bot_dir}/rasa/domain.yml", 'w', encoding='utf-8') as f:
        f.write(domain_content)
    
    # Create nlu.yml
    nlu_content = """version: "3.1"

nlu:
- intent: greet
  examples: |
    - здравейте
    - добър ден
    - здрасти
    - привет
    - може ли помощ
    - искам информация
    - какво правите
    - hello
    - hi
    - good morning

- intent: goodbye
  examples: |
    - благодаря
    - довиждане
    - чао
    - мерси
    - thanks
    - bye
    - приятен ден
    - до скоро
    - успех
    - всичко добро

- intent: ask_services
  examples: |
    - какво предлагате
    - какви услуги имате
    - с какво се занимавате
    - какво можете да направите
    - видове услуги
    - какво правите
    - услуги
    - предложения
    - какво предлагате за бизнеса ми
    - помощ за моя бизнес

- intent: ask_pricing
  examples: |
    - какви са цените
    - колко струва
    - цени
    - тарифи
    - пакети
    - колко коства
    - pricing
    - цената каква е
    - скъпо ли е
    - бюджет

- intent: ask_qr_menu
  examples: |
    - QR меню
    - дигитално меню
    - меню за ресторант
    - QR код меню
    - електронно меню
    - меню с QR код
    - дигитален каталог
    - безконтактно меню
    - мобилно меню
    - онлайн меню

- intent: ask_chatbots
  examples: |
    - чатбот
    - чат бот
    - автоматичен отговор
    - виртуален асистент
    - AI помощник
    - бот за сайт
    - разговорен бот
    - чатбот за фейсбук
    - социални мрежи бот
    - клиентски чат

- intent: ask_website
  examples: |
    - уебсайт
    - сайт
    - уеб страница
    - интернет страница
    - онлайн магазин
    - корпоративен сайт
    - бизнес сайт
    - изработка на сайт
    - нов сайт
    - редизайн

- intent: ask_seo
  examples: |
    - SEO
    - оптимизация
    - Google търсене
    - първа страница
    - класиране в Google
    - повече клиенти онлайн
    - видимост в интернет
    - digital marketing
    - онлайн маркетинг
    - сайт оптимизация

- intent: ask_telegram_bots
  examples: |
    - телеграм бот
    - автоматизация
    - telegram bot
    - работни процеси
    - автоматично обработване
    - интеграция
    - бизнес автоматизация
    - процеси
    - ефективност
    - telegram интеграция

- intent: ask_pwa
  examples: |
    - PWA
    - мобилно приложение
    - progressive web app
    - приложение
    - апликация
    - мобилен достъп
    - офлайн работа
    - приложение за телефон
    - уеб апликация
    - мобилна версия

- intent: ask_consultation
  examples: |
    - консултация
    - съвет
    - помощ
    - безплатна консултация
    - разговор
    - среща
    - планиране
    - стратегия
    - препоръки
    - анализ

- intent: ask_support
  examples: |
    - поддръжка
    - техническа помощ
    - проблем със сайт
    - не работи
    - грешка
    - support
    - помощ с проект
    - актуализация
    - редакция
    - промени

- intent: ask_contact
  examples: |
    - контакт
    - как да се свържа
    - телефон
    - имейл
    - адрес
    - връзка
    - информация за контакт
    - офис
    - местонахождение
    - как да ви намеря
"""
    
    with open(f"{bot_dir}/rasa/data/nlu.yml", 'w', encoding='utf-8') as f:
        f.write(nlu_content)
    
    # Create stories.yml
    stories_content = """version: "3.1"

stories:
- story: about services
  steps:
  - intent: greet
  - action: utter_greet
  - intent: ask_services
  - action: utter_services

- story: price inquiry
  steps:
  - intent: ask_pricing
  - action: utter_pricing

- story: qr menu inquiry
  steps:
  - intent: ask_qr_menu
  - action: utter_qr_menu

- story: chatbot inquiry
  steps:
  - intent: ask_chatbots
  - action: utter_chatbots

- story: website inquiry
  steps:
  - intent: ask_website
  - action: utter_website

- story: seo inquiry
  steps:
  - intent: ask_seo
  - action: utter_seo

- story: telegram bots inquiry
  steps:
  - intent: ask_telegram_bots
  - action: utter_telegram_bots

- story: pwa inquiry
  steps:
  - intent: ask_pwa
  - action: utter_pwa

- story: consultation inquiry
  steps:
  - intent: ask_consultation
  - action: utter_consultation

- story: support inquiry
  steps:
  - intent: ask_support
  - action: utter_support

- story: contact inquiry
  steps:
  - intent: ask_contact
  - action: utter_contact

- story: goodbye
  steps:
  - intent: goodbye
  - action: utter_goodbye
"""
    
    with open(f"{bot_dir}/rasa/data/stories.yml", 'w', encoding='utf-8') as f:
        f.write(stories_content)
    
    # Create config.yml
    config_content = """language: bg

pipeline:
  - name: WhitespaceTokenizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: char_wb
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100

policies:
  - name: MemoizationPolicy
  - name: RulePolicy
  - name: UnexpecTEDIntentPolicy
  - name: TEDPolicy
    max_history: 5
    epochs: 100
"""
    
    with open(f"{bot_dir}/rasa/config.yml", 'w', encoding='utf-8') as f:
        f.write(config_content)
    
    print("✅ DragonForgedDreams Bot V2 created successfully!")

if __name__ == "__main__":
    create_dragonforged_bot_v2()

