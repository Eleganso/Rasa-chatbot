#!/usr/bin/env python3
"""
DragonForgedDreams Bot - Version 1
Based on first data source
"""

import os
import yaml

def create_dragonforged_bot_v1():
    """Create DragonForgedDreams bot version 1"""
    
    # Create bot directory
    bot_dir = "bots/dragonforged_bot_v1"
    os.makedirs(f"{bot_dir}/rasa/data", exist_ok=True)
    os.makedirs(f"{bot_dir}/rasa/models", exist_ok=True)
    
    # Create domain.yml
    domain_content = """version: "3.1"

intents:
  - greet
  - goodbye
  - ask_about_services
  - ask_about_prices
  - ask_about_chatbots
  - ask_about_websites
  - ask_special_offers
  - ask_contact

entities:
  - service_type
  - package_name
  - contact_method

slots:
  service_type:
    type: text
    mappings:
    - type: from_entity
      entity: service_type
  package_name:
    type: text
    mappings:
    - type: from_entity
      entity: package_name
  contact_method:
    type: text
    mappings:
    - type: from_entity
      entity: contact_method

responses:
  utter_greet:
  - text: "Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?"
  - text: "Привет! Аз съм виртуалният ви асистент. Какво ви интересува от нашите услуги?"
  - text: "Добър ден! Готов съм да отговоря на въпросите ви за нашите дигитални решения!"

  utter_goodbye:
  - text: "Благодаря за интереса! Очакваме скоро да работим заедно. Приятен ден!"
  - text: "До скоро! Не забравяйте - безплатната консултация ви чака на dragonforgeddreams.com!"
  - text: "Чао! При нужда от дигитални решения, знаете къде да ни намерите!"

  utter_ask_about_services:
  - text: "В DragonForgedDreams предлагаме чатботове за сайтове и социални мрежи, уеб разработка, Telegram автоматизации, SEO оптимизация и техническа поддръжка."
  - text: "Ние създаваме умни решения за бизнеси: чатботове, сайтове, автоматизации и PWA приложения."
  - text: "Фокусът ни е върху дигитални решения – чатботове, изработка и поддръжка на сайтове, SEO оптимизация и консултации."

  utter_ask_about_prices:
  - text: "Може да видите всички наши пакети и цени на страницата ни: https://dragonforgeddreams.com/pricing"
  - text: "Имаме гъвкави пакети – стартов, професионален и signature. Пълни детайли: https://dragonforgeddreams.com/pricing"
  - text: "Цените ни зависят от пакета и услугата. Всички детайли в pricing секцията на сайта."

  utter_ask_about_chatbots:
  - text: "Да, създаваме чатботове за сайтове, социални мрежи и Telegram."
  - text: "Нашите чатботове могат да автоматизират поръчки, клиентска поддръжка и бизнес процеси."
  - text: "Изграждаме ботове, които работят за вас 24/7 – отговарят на клиенти, приемат заявки и интегрират с различни системи."

  utter_ask_about_websites:
  - text: "Предлагаме изграждане на модерни уебсайтове, онлайн магазини и PWA."
  - text: "Можем да създадем сайт според нуждите ви – корпоративен сайт, онлайн магазин или специализирано решение."
  - text: "Услугите ни включват и интеграции, SEO, както и поддръжка след старта."

  utter_ask_special_offers:
  - text: "Предлагаме безплатна консултация, за да изберем правилното решение за вашия бизнес."
  - text: "Може да запазите безплатна консултация още днес – ще ви помогнем да изберете пакет."
  - text: "Имаме персонализирани оферти за клиенти, в зависимост от нуждите и мащаба на бизнеса."

  utter_ask_contact:
  - text: "Може да се свържете с нас чрез формата за контакт на сайта или директно на имейл info@dragonforgeddreams.com"
  - text: "Налични сме за клиенти от цял свят – пишете ни чрез сайта."
  - text: "За консултация или поръчка, посетете секцията 'Контакт' на нашия сайт."

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

- intent: ask_about_services
  examples: |
    - какво предлагате
    - с какво се занимавате
    - услуги на dragonforgeddreams
    - можеш ли да ми кажеш какви услуги имате
    - какви решения предлагате за бизнеси
    - с какво може да ми помогнете
    - услуги за сайтове
    - предлагате ли чатботове
    - имате ли SEO оптимизация
    - как мога да автоматизирам бизнеса си с вас

- intent: ask_about_prices
  examples: |
    - колко струват услугите ви
    - имате ли абонаментни планове
    - колко е стартовия пакет
    - цена на професионалния план
    - каква е разликата между пакетите
    - ценова листа
    - искам информация за цената
    - покажи ми плановете ви
    - дай ми повече за signature пакета
    - колко струва поддръжката

- intent: ask_about_chatbots
  examples: |
    - правите ли чатботове
    - искам бот за сайта ми
    - мога ли да имам бот за Telegram
    - как работят вашите чатботове
    - какво може да прави чатбот, ако го поръчам от вас
    - автоматизация с ботове
    - бот за социални мрежи
    - колко време отнема направата на бот
    - поддържате ли ботове след като ги направите
    - може ли ботът да приема поръчки

- intent: ask_about_websites
  examples: |
    - правите ли сайтове
    - колко струва сайт при вас
    - искам корпоративен сайт
    - можете ли да направите онлайн магазин
    - интересува ме уебсайт за ресторант
    - изграждате ли мобилни приложения или PWA
    - SEO услуги предлагате ли за сайтове
    - поддръжка на сайт извършвате ли
    - интегрирате ли плащания
    - работите ли със WordPress

- intent: ask_special_offers
  examples: |
    - имате ли безплатна консултация
    - оферти за нови клиенти
    - как мога да получа консултация
    - има ли промоция за абонамент
    - мога ли да пробвам услугата ви
    - предлагате ли тестов период
    - интересувам се от консултация
    - как да получа персонална оферта
    - правите ли отстъпки за годишен абонамент
    - мога ли да комбинирам услуги

- intent: ask_contact
  examples: |
    - как да се свържа с вас
    - телефон за връзка
    - имате ли имейл
    - работите ли с клиенти извън България
    - как да поръчам услуга
    - начин за контакт
    - къде мога да ви пиша
    - имате ли форма за контакт
    - имате ли екип за поддръжка
    - как да започнем работа
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
  - intent: ask_about_services
  - action: utter_ask_about_services

- story: price inquiry
  steps:
  - intent: ask_about_prices
  - action: utter_ask_about_prices

- story: chatbot inquiry
  steps:
  - intent: ask_about_chatbots
  - action: utter_ask_about_chatbots

- story: website inquiry
  steps:
  - intent: ask_about_websites
  - action: utter_ask_about_websites

- story: special offers inquiry
  steps:
  - intent: ask_special_offers
  - action: utter_ask_special_offers

- story: contact inquiry
  steps:
  - intent: ask_contact
  - action: utter_ask_contact

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
    
    print("✅ DragonForgedDreams Bot V1 created successfully!")

if __name__ == "__main__":
    create_dragonforged_bot_v1()

