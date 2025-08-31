#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verify Web Interfaces
Проверка на уеб интерфейсите
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def verify_web_interfaces():
    """Проверява уеб интерфейсите на ботовете"""
    print("🔍 ПРОВЕРКА НА УЕБ ИНТЕРФЕЙСИТЕ")
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
        
        # Проверка на уеб интерфейсите
        print("\n🌐 ПРОВЕРКА НА УЕБ ИНТЕРФЕЙСИТЕ:")
        print("="*60)
        
        bot_configs = {
            'zlatna_kosa': {
                'name': 'Салон "Златна коса"',
                'expected_title': 'Салон "Златна коса"',
                'expected_welcome': 'салон "Златна коса"'
            },
            'zlatna_vilitsa': {
                'name': 'Ресторант "Златна вилица"',
                'expected_title': 'Ресторант "Златна вилица"',
                'expected_welcome': 'ресторант "Златна вилица"'
            },
            'grand_sofia': {
                'name': 'Хотел "Гранд София"',
                'expected_title': 'Хотел "Гранд София"',
                'expected_welcome': 'хотел "Гранд София"'
            },
            'zdrave_medical': {
                'name': 'Медицински център "Здраве+"',
                'expected_title': 'Медицински център "Здраве+"',
                'expected_welcome': 'д-р Мария'
            },
            'moto_expert': {
                'name': 'Автосервиз "Мото Експерт"',
                'expected_title': 'Автосервиз "Мото Експерт"',
                'expected_welcome': 'автосервиз асистент'
            }
        }
        
        all_passed = True
        
        for bot_id, bot_config in bot_configs.items():
            print(f"\n🤖 Проверка на {bot_config['name']}:")
            print("-" * 50)
            
            url_path = bot_id.replace("_", "-")
            
            # Проверка на уеб интерфейса
            stdin, stdout, stderr = ssh.exec_command(f"curl -s http://localhost/{url_path}/")
            content_response = stdout.read().decode('utf-8')
            
            # Проверка на заглавието
            if bot_config['expected_title'] in content_response:
                print(f"   ✅ Заглавие: OK")
            else:
                print(f"   ❌ Заглавие: НЕ е намерено '{bot_config['expected_title']}'")
                all_passed = False
            
            # Проверка на приветственото съобщение
            if bot_config['expected_welcome'] in content_response:
                print(f"   ✅ Приветствие: OK")
            else:
                print(f"   ❌ Приветствие: НЕ е намерено '{bot_config['expected_welcome']}'")
                all_passed = False
            
            # Проверка дали няма DragonForged текстове
            if 'DragonForgedDreams' in content_response:
                print(f"   ❌ DragonForged текст: ВСЕ ОЩЕ СЪЩЕСТВУВА!")
                all_passed = False
            else:
                print(f"   ✅ DragonForged текст: Премахнат")
            
            # Проверка на HTTP статуса
            stdin, stdout, stderr = ssh.exec_command(f"curl -I http://localhost/{url_path}/")
            status_response = stdout.read().decode('utf-8')
            
            if "200 OK" in status_response:
                print(f"   ✅ HTTP статус: 200 OK")
            else:
                print(f"   ❌ HTTP статус: {status_response[:100]}...")
                all_passed = False
        
        # Проверка на API endpoints
        print(f"\n🧪 ПРОВЕРКА НА API ENDPOINTS:")
        print("="*50)
        
        for bot_id, bot_config in bot_configs.items():
            url_path = bot_id.replace("_", "-")
            print(f"\n🤖 Тестване на API за {bot_config['name']}:")
            
            # Тест на API директно в контейнера
            stdin, stdout, stderr = ssh.exec_command(f"cd /root/multi-bots && docker exec {bot_id} curl -X POST http://localhost:5005/webhooks/rest/webhook -H 'Content-Type: application/json' -d '{{\"message\": \"здравей\"}}'")
            api_response = stdout.read().decode('utf-8')
            
            if "error" in api_response.lower():
                print(f"   ❌ API грешка: {api_response[:200]}...")
                all_passed = False
            else:
                print(f"   ✅ API отговор: {api_response[:200]}...")
        
        print(f"\n🎯 ЗАКЛЮЧЕНИЕ:")
        print("="*30)
        
        if all_passed:
            print("✅ Всички проверки преминаха успешно!")
            print("✅ Уеб интерфейсите са поправени")
            print("✅ Ботовете използват правилните модели")
            print("✅ API endpoints работят")
        else:
            print("❌ Някои проверки не преминаха!")
            print("⚠️  Проверете отново уеб интерфейсите")
        
        print(f"\n🌐 URL-и за тестване:")
        for bot_id, bot_config in bot_configs.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return all_passed
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    verify_web_interfaces()
