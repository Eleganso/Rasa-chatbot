#!/usr/bin/env python3
"""
Fix NLU YAML formatting
"""

import yaml
import re

def fix_nlu_file():
    """Fix the NLU YAML file formatting"""
    
    # Read the current file
    with open('rasa/data/nlu.yml', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix the examples formatting
    # Replace the problematic examples sections
    new_intents = """
- intent: weather
  examples: |
    - what's the weather like
    - how's the weather
    - weather forecast
    - is it raining
    - temperature today
    - weather today
    - what's the temperature
    - is it sunny
    - weather report
    - климатични условия
    - какво е времето
    - времето днес
    - ще вали ли
    - температурата

- intent: help
  examples: |
    - help
    - I need help
    - can you help me
    - what can you do
    - how can you help
    - assistance
    - support
    - помощ
    - нужна ми е помощ
    - можеш ли да ми помогнеш
    - какво можеш да правиш

- intent: thanks
  examples: |
    - thanks
    - thank you
    - thanks a lot
    - thank you very much
    - thanks so much
    - благодаря
    - мерси
    - благодаря ти
    - много благодаря

- intent: joke
  examples: |
    - tell me a joke
    - say something funny
    - make me laugh
    - joke
    - funny story
    - разкажи ми виц
    - кажи нещо забавно
    - разсмеши ме
    - виц

- intent: time
  examples: |
    - what time is it
    - current time
    - time now
    - what's the time
    - колко е часът
    - текущо време
    - сегашно време
    - часът

- intent: name
  examples: |
    - what's your name
    - what should I call you
    - who are you
    - your name
    - как се казваш
    - какво е твоето име
    - кой си ти
    - твоето име

- intent: capabilities
  examples: |
    - what can you do
    - your capabilities
    - what are your features
    - what do you do
    - какво можеш да правиш
    - твоите възможности
    - какви са функциите ти
    - какво правиш
"""
    
    # Remove the problematic intents and add the correct ones
    # Find where the original intents end
    lines = content.split('\n')
    new_lines = []
    skip_until_end = False
    
    for line in lines:
        if line.strip().startswith('- intent: weather'):
            skip_until_end = True
            continue
        elif skip_until_end and line.strip() == '':
            skip_until_end = False
            new_lines.append(line)
            new_lines.append(new_intents.strip())
            continue
        elif skip_until_end:
            continue
        else:
            new_lines.append(line)
    
    # Write the fixed content
    with open('rasa/data/nlu.yml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print("✅ Fixed NLU YAML formatting")

if __name__ == "__main__":
    fix_nlu_file()
