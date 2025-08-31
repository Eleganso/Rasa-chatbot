#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Train New Bots Locally
Трениране на новите ботове локално
"""

import os
import subprocess
import json
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def train_bot(bot_id, bot_config):
    """Тренира конкретен бот"""
    print(f"\n🤖 Трениране на {bot_config['name']}...")
    print("="*50)
    
    rasa_path = bot_config['path']
    print(f"📍 Път: {rasa_path}")
    
    # Проверка дали директорията съществува
    if not os.path.exists(rasa_path):
        print(f"❌ Директорията {rasa_path} не съществува!")
        return False
    
    # Проверка на необходимите файлове
    required_files = ['config.yml', 'domain.yml', 'data/nlu.yml', 'data/stories.yml']
    missing_files = []
    
    for file in required_files:
        file_path = os.path.join(rasa_path, file)
        if not os.path.exists(file_path):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Липсват файлове: {', '.join(missing_files)}")
        return False
    
    try:
        # Създаване на models директория ако не съществува
        models_dir = os.path.join(rasa_path, 'models')
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)
            print(f"📁 Създадена директория: {models_dir}")
        
        # Трениране с Docker
        print("📚 Стартиране на трениране с Docker...")
        cmd = [
            'docker', 'run', '--rm', 
            '-v', f'{os.path.abspath(rasa_path)}:/app',
            'rasa/rasa:3.6.21', 'train', '--force'
        ]
        
        print(f"🔧 Команда: {' '.join(cmd)}")
        
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=rasa_path)
        
        if result.returncode == 0:
            print("✅ Тренирането завършено успешно!")
            
            # Проверка на създадения модел
            models = [f for f in os.listdir(models_dir) if f.endswith('.tar.gz')]
            if models:
                latest_model = max(models, key=lambda x: os.path.getctime(os.path.join(models_dir, x)))
                print(f"📦 Създаден модел: {latest_model}")
                return True
            else:
                print("❌ Не е намерен създаден модел!")
                return False
        else:
            print(f"❌ Грешка при трениране:")
            print(f"STDOUT: {result.stdout}")
            print(f"STDERR: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

def train_all_new_bots():
    """Тренира всички нови ботове"""
    print("🚀 ТРЕНИРАНЕ НА ВСИЧКИ НОВИ БОТОВЕ")
    print("="*60)
    
    config = load_config()
    
    # Списък на новите ботове (без dragonforged_v2)
    new_bots = {
        'zlatna_kosa': config['bots']['zlatna_kosa'],
        'zlatna_vilitsa': config['bots']['zlatna_vilitsa'],
        'grand_sofia': config['bots']['grand_sofia'],
        'zdrave_medical': config['bots']['zdrave_medical'],
        'moto_expert': config['bots']['moto_expert']
    }
    
    success_count = 0
    failed_bots = []
    
    for bot_id, bot_config in new_bots.items():
        if train_bot(bot_id, bot_config):
            success_count += 1
        else:
            failed_bots.append(bot_config['name'])
    
    print(f"\n📊 РЕЗУЛТАТ:")
    print(f"✅ Успешно тренирани: {success_count}/{len(new_bots)}")
    
    if failed_bots:
        print(f"❌ Неуспешни: {', '.join(failed_bots)}")
    
    if success_count == len(new_bots):
        print("\n🎉 Всички ботове са тренирани успешно!")
        print("\n📤 Следваща стъпка: Качване на моделите на VPS")
        return True
    else:
        print(f"\n⚠️  {len(failed_bots)} бота не са тренирани успешно!")
        return False

if __name__ == "__main__":
    train_all_new_bots()
