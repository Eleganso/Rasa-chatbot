#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update Nginx for Static Files
Обновяване на Nginx за статични файлове
"""

import paramiko
import time

def update_nginx_static():
    """Обновява Nginx за статични файлове"""
    print("🔧 ОБНОВЯВАНЕ НА NGINX ЗА СТАТИЧНИ ФАЙЛОВЕ")
    print("="*50)
    
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
        
        # Създаване на нова Nginx конфигурация
        print("\n🔧 Създаване на нова Nginx конфигурация...")
        
        nginx_config = """events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    upstream zlatna_kosa {
        server zlatna_kosa:5005;
    }
    
    upstream zlatna_vilitsa {
        server zlatna_vilitsa:5008;
    }
    
    upstream grand_sofia {
        server grand_sofia:5009;
    }
    
    upstream zdrave_medical {
        server zdrave_medical:5010;
    }
    
    upstream moto_expert {
        server moto_expert:5011;
    }
    
    upstream dragonforged_v2 {
        server dragonforged_v2:5005;
    }
    
    server {
        listen 80;
        server_name 37.60.225.86;
        
        # Салон Златна коса - статичен файл
        location = /zlatna-kosa/ {
            alias /root/multi-bots/bots/zlatna_kosa_salon/web/index.html;
            default_type text/html;
        }
        
        location /zlatna-kosa/webhooks/rest/webhook {
            proxy_pass http://zlatna_kosa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Ресторант Златна вилица - статичен файл
        location = /zlatna-vilitsa/ {
            alias /root/multi-bots/bots/zlatna_vilitsa_restaurant/web/index.html;
            default_type text/html;
        }
        
        location /zlatna-vilitsa/webhooks/rest/webhook {
            proxy_pass http://zlatna_vilitsa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Хотел Гранд София - статичен файл
        location = /grand-sofia/ {
            alias /root/multi-bots/bots/grand_sofia_hotel/web/index.html;
            default_type text/html;
        }
        
        location /grand-sofia/webhooks/rest/webhook {
            proxy_pass http://grand_sofia/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Медицински център Здраве+ - статичен файл
        location = /zdrave-medical/ {
            alias /root/multi-bots/bots/zdrave_medical_center/web/index.html;
            default_type text/html;
        }
        
        location /zdrave-medical/webhooks/rest/webhook {
            proxy_pass http://zdrave_medical/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Автосервиз Мото Експерт - статичен файл
        location = /moto-expert/ {
            alias /root/multi-bots/bots/moto_expert_autoservice/web/index.html;
            default_type text/html;
        }
        
        location /moto-expert/webhooks/rest/webhook {
            proxy_pass http://moto_expert/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # DragonForged V2
        location /dragonforged-v2/ {
            proxy_pass http://dragonforged_v2/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        location /dragonforged-v2/webhooks/rest/webhook {
            proxy_pass http://dragonforged_v2/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Статични файлове
        location / {
            root /var/www/html;
            index index.html;
            try_files $uri $uri/ =404;
        }
    }
}
"""
        
        # Записване на новата конфигурация
        ssh.exec_command("cd /root/multi-bots && echo '" + nginx_config.replace("'", "'\"'\"'") + "' > nginx.conf")
        
        # Стартиране на контейнерите
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        # Тестване на уеб интерфейсите
        print("\n🧪 ТЕСТИРАНЕ НА УЕБ ИНТЕРФЕЙСИТЕ:")
        print("="*50)
        
        test_urls = [
            ('zlatna-kosa', 'Салон "Златна коса"'),
            ('zlatna-vilitsa', 'Ресторант "Златна вилица"'),
            ('grand-sofia', 'Хотел "Гранд София"'),
            ('zdrave-medical', 'Медицински център "Здраве+"'),
            ('moto-expert', 'Автосервиз "Мото Експерт"')
        ]
        
        for url_path, bot_name in test_urls:
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
        
        print(f"\n🎉 Обновяването завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for url_path, bot_name in test_urls:
            print(f"   {bot_name}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    update_nginx_static()
