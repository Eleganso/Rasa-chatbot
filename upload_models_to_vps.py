#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Upload Trained Models to VPS
Качване на тренираните модели на VPS
"""

import json
import os
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def upload_models_to_vps():
    """Качва тренираните модели на VPS"""
    print("📤 КАЧВАНЕ НА МОДЕЛИ НА VPS")
    print("="*50)
    
    config = load_config()
    host = "37.60.225.86"
    username = input("Потребителско име (root): ").strip() or "root"
    password = input("Парола: ").strip()
    
    try:
        # Свързване с VPS
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        print("✅ Успешно свързване!")
        
        # Спиране на контейнерите
        print("\n🛑 Спиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose down")
        time.sleep(5)
        
        # Качване на моделите
        print("\n📤 Качване на модели...")
        sftp = ssh.open_sftp()
        
        new_bots = {
            'zlatna_kosa': config['bots']['zlatna_kosa'],
            'zlatna_vilitsa': config['bots']['zlatna_vilitsa'],
            'grand_sofia': config['bots']['grand_sofia'],
            'zdrave_medical': config['bots']['zdrave_medical'],
            'moto_expert': config['bots']['moto_expert']
        }
        
        for bot_id, bot_config in new_bots.items():
            print(f"\n📤 Качване на модели за {bot_config['name']}...")
            
            local_models_dir = os.path.join(bot_config['path'], 'models')
            remote_models_dir = f"/root/multi-bots/{bot_config['path']}/models"
            
            # Проверка дали има модели локално
            if not os.path.exists(local_models_dir):
                print(f"   ⚠️  Няма models директория за {bot_id}")
                continue
            
            # Създаване на remote models директория
            ssh.exec_command(f"mkdir -p {remote_models_dir}")
            
            # Качване на всички модели
            models = [f for f in os.listdir(local_models_dir) if f.endswith('.tar.gz')]
            if not models:
                print(f"   ⚠️  Няма модели в {local_models_dir}")
                continue
            
            for model_file in models:
                local_model_path = os.path.join(local_models_dir, model_file)
                remote_model_path = f"{remote_models_dir}/{model_file}"
                
                print(f"   📦 Качване на {model_file}...")
                sftp.put(local_model_path, remote_model_path)
                print(f"   ✅ {model_file} качен успешно!")
        
        sftp.close()
        
        # Стартиране на контейнерите отново
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        # Проверка на статуса
        print("\n✅ Проверка на статуса...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Тестване на API endpoints
        print("\n🧪 Тестване на API endpoints...")
        for bot_id, bot_config in new_bots.items():
            url_path = bot_id.replace("_", "-")
            api_url = f"http://localhost/{url_path}/webhooks/rest/webhook"
            print(f"Тестване на {bot_config['name']}: {api_url}")
            
            stdin, stdout, stderr = ssh.exec_command(f"curl -X POST {api_url} -H 'Content-Type: application/json' -d '{{\"message\": \"здравей\"}}'")
            response = stdout.read().decode('utf-8')
            print(f"Отговор: {response[:200]}...")
        
        print("\n🎉 Качването завършено успешно!")
        print("\n📋 Ботове с нови модели:")
        for bot_id, bot_config in new_bots.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    upload_models_to_vps()
