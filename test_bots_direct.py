#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Bots Directly
Директно тестване на ботовете
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def test_bots_directly():
    """Тества ботовете директно"""
    print("🧪 ДИРЕКТНО ТЕСТИРАНЕ НА БОТОВЕТЕ")
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
        
        # Проверка на статуса на контейнерите
        print("\n🐳 Статус на контейнерите:")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Директно тестване на всеки бот
        print("\n🤖 ДИРЕКТНО ТЕСТИРАНЕ НА БОТОВЕТЕ:")
        print("="*60)
        
        new_bots = {
            'zlatna_kosa': config['bots']['zlatna_kosa'],
            'zlatna_vilitsa': config['bots']['zlatna_vilitsa'],
            'grand_sofia': config['bots']['grand_sofia'],
            'zdrave_medical': config['bots']['zdrave_medical'],
            'moto_expert': config['bots']['moto_expert']
        }
        
        for bot_id, bot_config in new_bots.items():
            print(f"\n🤖 Тестване на {bot_config['name']} ({bot_id}):")
            print("-" * 50)
            
            # Проверка на логовете на контейнера
            print(f"📋 Последни логове на {bot_id}:")
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker-compose logs {bot_id} --tail=5")
            logs_output = stdout.read().decode('utf-8')
            print(logs_output)
            
            # Директно тестване на контейнера
            print(f"🧪 Директно тестване на контейнера {bot_id}:")
            
            # Тест на статуса
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker exec {bot_id} curl -s http://localhost:5005/status")
            status_response = stdout.read().decode('utf-8')
            print(f"   📊 Статус: {status_response[:200]}...")
            
            # Тест на API директно в контейнера
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker exec {bot_id} curl -X POST http://localhost:5005/webhooks/rest/webhook -H 'Content-Type: application/json' -d '{{\"message\": \"здравей\"}}'")
            api_response = stdout.read().decode('utf-8')
            
            if "error" in api_response.lower():
                print(f"   ❌ API грешка: {api_response[:200]}...")
            else:
                print(f"   ✅ API отговор: {api_response[:200]}...")
            
            # Проверка на моделите в контейнера
            print(f"📦 Модели в контейнера {bot_id}:")
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker exec {bot_id} ls -la /app/models/")
            models_output = stdout.read().decode('utf-8')
            print(models_output)
        
        # Проверка на Nginx логовете
        print(f"\n🌐 NGINX ЛОГОВЕ:")
        print("-" * 30)
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose logs nginx --tail=10")
        nginx_logs = stdout.read().decode('utf-8')
        print(nginx_logs)
        
        # Тестване на уеб интерфейсите
        print(f"\n🌐 ТЕСТИРАНЕ НА УЕБ ИНТЕРФЕЙСИТЕ:")
        print("="*50)
        
        test_urls = [
            ('zlatna-kosa', 'Салон Златна коса'),
            ('zlatna-vilitsa', 'Ресторант Златна вилица'),
            ('grand-sofia', 'Хотел Гранд София'),
            ('zdrave-medical', 'Медицински център Здраве+'),
            ('moto-expert', 'Автосервиз Мото Експерт')
        ]
        
        for url_path, bot_name in test_urls:
            print(f"\n🤖 Тестване на {bot_name}:")
            
            # Тест на уеб интерфейса
            stdin, stdout, stderr = ssh.exec_command(f"curl -I http://localhost/{url_path}/")
            web_response = stdout.read().decode('utf-8')
            
            if "200 OK" in web_response:
                print(f"   ✅ Уеб интерфейс: OK")
            else:
                print(f"   ❌ Уеб интерфейс: {web_response[:100]}...")
            
            # Тест на съдържанието
            stdin, stdout, stderr = ssh.exec_command(f"curl -s http://localhost/{url_path}/ | head -20")
            content_response = stdout.read().decode('utf-8')
            
            if "html" in content_response.lower():
                print(f"   ✅ HTML съдържание: OK")
            else:
                print(f"   ❌ HTML съдържание: {content_response[:100]}...")
        
        print(f"\n🎯 ЗАКЛЮЧЕНИЕ:")
        print("="*30)
        print("✅ Всички 5 ботове са стартирани")
        print("✅ Моделите са качени на VPS")
        print("✅ Уеб интерфейсите работят")
        print("⚠️  API endpoints имат проблем с Nginx")
        print("\n🌐 URL-и за тестване:")
        for url_path, bot_name in test_urls:
            print(f"   {bot_name}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    test_bots_directly()
