#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Force Reload Nginx
Принудително презареждане на Nginx
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def force_reload_nginx():
    """Принудително презарежда Nginx"""
    print("🔄 ПРИНУДИТЕЛНО ПРЕЗАРЕЖДАНЕ НА NGINX")
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
        
        # Спиране на всички контейнери
        print("\n🛑 Спиране на всички контейнери...")
        ssh.exec_command("cd /root/multi-bots && docker-compose down")
        time.sleep(5)
        
        # Изчистване на Docker кеша
        print("\n🧹 Изчистване на Docker кеша...")
        ssh.exec_command("docker system prune -f")
        time.sleep(3)
        
        # Проверка на файловете
        print("\n📁 Проверка на index.html файловете:")
        
        bot_configs = {
            'zlatna_kosa': 'Салон "Златна коса"',
            'zlatna_vilitsa': 'Ресторант "Златна вилица"',
            'grand_sofia': 'Хотел "Гранд София"',
            'zdrave_medical': 'Медицински център "Здраве+"',
            'moto_expert': 'Автосервиз "Мото Експерт"'
        }
        
        for bot_id, bot_name in bot_configs.items():
            print(f"\n🤖 Проверка на {bot_name}:")
            
            # Проверка на съдържанието на файла
            remote_web_dir = f"/root/multi-bots/bots/{bot_id}/web"
            stdin, stdout, stderr = ssh.exec_command(f"head -10 {remote_web_dir}/index.html")
            file_content = stdout.read().decode('utf-8')
            
            if bot_name in file_content:
                print(f"   ✅ Файлът съдържа правилното заглавие")
            else:
                print(f"   ❌ Файлът НЕ съдържа правилното заглавие")
                print(f"   📄 Първите 10 реда: {file_content[:200]}...")
        
        # Стартиране на контейнерите отново
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(30)
        
        # Принудително презареждане на Nginx
        print("\n🔄 Принудително презареждане на Nginx...")
        ssh.exec_command("cd /root/multi-bots && docker-compose restart nginx")
        time.sleep(10)
        
        # Проверка на статуса
        print("\n📊 Статус на контейнерите:")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Тестване на уеб интерфейсите
        print("\n🧪 ТЕСТИРАНЕ НА УЕБ ИНТЕРФЕЙСИТЕ:")
        print("="*50)
        
        for bot_id, bot_name in bot_configs.items():
            url_path = bot_id.replace("_", "-")
            print(f"\n🤖 Тестване на {bot_name}:")
            
            # Тест на уеб интерфейса
            stdin, stdout, stderr = ssh.exec_command(f"curl -s http://localhost/{url_path}/ | grep -i '{bot_name}'")
            content_response = stdout.read().decode('utf-8')
            
            if bot_name in content_response:
                print(f"   ✅ Правилно заглавие: OK")
            else:
                print(f"   ❌ Грешно заглавие")
            
            # Тест на приветственото съобщение
            if 'DragonForgedDreams' in content_response:
                print(f"   ❌ DragonForged текст: ВСЕ ОЩЕ СЪЩЕСТВУВА!")
            else:
                print(f"   ✅ DragonForged текст: Премахнат")
        
        print(f"\n🎉 Презареждането завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for bot_id, bot_name in bot_configs.items():
            url_path = bot_id.replace("_", "-")
            print(f"   {bot_name}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    force_reload_nginx()
