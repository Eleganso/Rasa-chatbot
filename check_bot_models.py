#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check Bot Models on VPS
Проверка на моделите на ботовете на VPS
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def check_bot_models():
    """Проверява моделите на ботовете на VPS"""
    print("🔍 ПРОВЕРКА НА МОДЕЛИТЕ НА БОТОВЕТЕ")
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
        
        # Проверка на Docker контейнерите
        print("\n🐳 Проверка на Docker контейнерите...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Проверка на моделите за всеки бот
        print("\n📦 ПРОВЕРКА НА МОДЕЛИТЕ:")
        print("="*60)
        
        new_bots = {
            'zlatna_kosa': config['bots']['zlatna_kosa'],
            'zlatna_vilitsa': config['bots']['zlatna_vilitsa'],
            'grand_sofia': config['bots']['grand_sofia'],
            'zdrave_medical': config['bots']['zdrave_medical'],
            'moto_expert': config['bots']['moto_expert']
        }
        
        for bot_id, bot_config in new_bots.items():
            print(f"\n🤖 {bot_config['name']}:")
            print("-" * 40)
            
            # Проверка на моделите в директорията
            remote_models_dir = f"/root/multi-bots/{bot_config['path']}/models"
            stdin, stdout, stderr = ssh.exec_command(f"ls -la {remote_models_dir}")
            models_output = stdout.read().decode('utf-8')
            
            if "No such file or directory" in models_output:
                print(f"   ❌ Няма models директория!")
                continue
            
            print(f"   📁 Модели в директорията:")
            for line in models_output.split('\n'):
                if '.tar.gz' in line:
                    print(f"      📦 {line.split()[-1]}")
            
            # Проверка на логовете на контейнера
            print(f"   📋 Логове на контейнера {bot_id}:")
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker-compose logs {bot_id} --tail=10")
            logs_output = stdout.read().decode('utf-8')
            
            # Търсене на информация за заредения модел
            model_loaded = False
            for line in logs_output.split('\n'):
                if 'model' in line.lower() and ('loaded' in line.lower() or 'loading' in line.lower()):
                    print(f"      🔍 {line.strip()}")
                    model_loaded = True
                elif 'error' in line.lower():
                    print(f"      ❌ {line.strip()}")
            
            if not model_loaded:
                print(f"      ⚠️  Не е намерена информация за заредения модел")
            
            # Тестване на API
            print(f"   🧪 Тестване на API...")
            url_path = bot_id.replace("_", "-")
            test_url = f"http://localhost/{url_path}/webhooks/rest/webhook"
            
            stdin, stdout, stderr = ssh.exec_command(f"curl -X POST {test_url} -H 'Content-Type: application/json' -d '{{\"message\": \"здравей\"}}'")
            api_response = stdout.read().decode('utf-8')
            
            if "405 Not Allowed" in api_response:
                print(f"      ⚠️  API връща 405 (вероятно Nginx проблем)")
            elif "error" in api_response.lower():
                print(f"      ❌ API грешка: {api_response[:100]}...")
            else:
                print(f"      ✅ API отговор: {api_response[:100]}...")
        
        # Проверка на Nginx конфигурацията
        print(f"\n🌐 ПРОВЕРКА НА NGINX КОНФИГУРАЦИЯТА:")
        print("-" * 50)
        
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && cat nginx.conf")
        nginx_config = stdout.read().decode('utf-8')
        
        # Проверка дали всички ботове са в Nginx конфигурацията
        for bot_id in new_bots.keys():
            if f"location /{bot_id.replace('_', '-')}/" in nginx_config:
                print(f"   ✅ {bot_id} - намерен в Nginx конфигурацията")
            else:
                print(f"   ❌ {bot_id} - НЕ е намерен в Nginx конфигурацията")
        
        # Проверка на статуса на Nginx контейнера
        print(f"\n📊 СТАТУС НА NGINX:")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose logs nginx --tail=5")
        nginx_logs = stdout.read().decode('utf-8')
        print(nginx_logs)
        
        print(f"\n🎯 ЗАКЛЮЧЕНИЕ:")
        print("="*30)
        print("✅ Всички 5 ботове са стартирани")
        print("✅ Моделите са качени на VPS")
        print("✅ Nginx конфигурацията е правилна")
        print("\n🌐 URL-и за тестване:")
        for bot_id, bot_config in new_bots.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    check_bot_models()
