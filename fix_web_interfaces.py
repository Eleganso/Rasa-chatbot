#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Web Interfaces
Поправяне на уеб интерфейсите на ботовете
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def fix_web_interfaces():
    """Поправя уеб интерфейсите на ботовете"""
    print("🔧 ПОПРАВЯНЕ НА УЕБ ИНТЕРФЕЙСИТЕ")
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
        
        # Поправяне на уеб интерфейсите
        print("\n🔧 Поправяне на уеб интерфейсите...")
        
        new_bots = {
            'zlatna_kosa': config['bots']['zlatna_kosa'],
            'zlatna_vilitsa': config['bots']['zlatna_vilitsa'],
            'grand_sofia': config['bots']['grand_sofia'],
            'zdrave_medical': config['bots']['zdrave_medical'],
            'moto_expert': config['bots']['moto_expert']
        }
        
        for bot_id, bot_config in new_bots.items():
            print(f"\n🤖 Поправяне на {bot_config['name']}...")
            
            # Четене на текущия index.html
            remote_web_dir = f"/root/multi-bots/{bot_config['path']}/web"
            stdin, stdout, stderr = ssh.exec_command(f"cat {remote_web_dir}/index.html")
            current_html = stdout.read().decode('utf-8')
            
            # Замяна на DragonForged текстове със специфични за бота
            updated_html = current_html
            
            # Замяна на заглавието
            updated_html = updated_html.replace(
                'DragonForgedDreams Bot V2',
                bot_config['name']
            )
            
            # Замяна на описанието
            updated_html = updated_html.replace(
                'Детайлни услуги и цени - QR меню, PWA, Telegram ботове',
                bot_config.get('description', 'Чатбот за вашите нужди')
            )
            
            # Замяна на чат статуса
            updated_html = updated_html.replace(
                'Чат с DragonForgedDreams Bot V2',
                f'Чат с {bot_config["name"]}'
            )
            
            # Замяна на приветственото съобщение
            if bot_id == 'zlatna_kosa':
                updated_html = updated_html.replace(
                    'Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?',
                    'Привет! ✨ Добре дошли в салон "Златна коса"! Как мога да ви помогна днес?'
                )
            elif bot_id == 'zlatna_vilitsa':
                updated_html = updated_html.replace(
                    'Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?',
                    'Добре дошли в ресторант "Златна вилица"! 🍽️ Как мога да ви помогна днес?'
                )
            elif bot_id == 'grand_sofia':
                updated_html = updated_html.replace(
                    'Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?',
                    'Добре дошли в хотел "Гранд София"! 🏨 Как мога да ви помогна днес?'
                )
            elif bot_id == 'zdrave_medical':
                updated_html = updated_html.replace(
                    'Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?',
                    'Здравейте! 👋 Аз съм д-р Мария, ваш виртуален асистент. Как мога да ви помогна?'
                )
            elif bot_id == 'moto_expert':
                updated_html = updated_html.replace(
                    'Здравейте! Добре дошли в DragonForgedDreams! Как мога да ви помогна днес?',
                    'Здравейте! 👋 Аз съм вашият виртуален автосервиз асистент. Как мога да ви помогна?'
                )
            
            # Записване на обновения файл
            ssh.exec_command(f"echo '{updated_html.replace(chr(39), chr(39) + chr(34) + chr(39) + chr(34) + chr(39))}' > {remote_web_dir}/index.html")
            
            print(f"   ✅ {bot_config['name']} - поправен")
        
        # Стартиране на контейнерите отново
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        # Тестване на уеб интерфейсите
        print("\n🧪 ТЕСТИРАНЕ НА УЕБ ИНТЕРФЕЙСИТЕ:")
        print("="*50)
        
        for bot_id, bot_config in new_bots.items():
            url_path = bot_id.replace("_", "-")
            print(f"\n🤖 Тестване на {bot_config['name']}:")
            
            # Тест на уеб интерфейса
            stdin, stdout, stderr = ssh.exec_command(f"curl -s http://localhost/{url_path}/ | grep -i '{bot_config['name']}'")
            content_response = stdout.read().decode('utf-8')
            
            if bot_config['name'] in content_response:
                print(f"   ✅ Правилно заглавие: OK")
            else:
                print(f"   ❌ Грешно заглавие")
            
            # Тест на приветственото съобщение
            if bot_id == 'zlatna_kosa' and 'салон "Златна коса"' in content_response:
                print(f"   ✅ Правилно приветствие: OK")
            elif bot_id == 'zlatna_vilitsa' and 'ресторант "Златна вилица"' in content_response:
                print(f"   ✅ Правилно приветствие: OK")
            elif bot_id == 'grand_sofia' and 'хотел "Гранд София"' in content_response:
                print(f"   ✅ Правилно приветствие: OK")
            elif bot_id == 'zdrave_medical' and 'д-р Мария' in content_response:
                print(f"   ✅ Правилно приветствие: OK")
            elif bot_id == 'moto_expert' and 'автосервиз асистент' in content_response:
                print(f"   ✅ Правилно приветствие: OK")
            else:
                print(f"   ❌ Грешно приветствие")
        
        print(f"\n🎉 Поправянето завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for bot_id, bot_config in new_bots.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    fix_web_interfaces()
