#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix Nginx API Configuration
Поправяне на Nginx API конфигурацията
"""

import paramiko
import time

def fix_nginx_api():
    """Поправя Nginx API конфигурацията"""
    print("🔧 ПОПРАВЯНЕ НА NGINX API КОНФИГУРАЦИЯТА")
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
        
        # Създаване на нова Nginx конфигурация с правилни API endpoints
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
        
        # Салон Златна коса
        location /zlatna-kosa/ {
            proxy_pass http://zlatna_kosa/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        location /zlatna-kosa/webhooks/rest/webhook {
            proxy_pass http://zlatna_kosa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Ресторант Златна вилица
        location /zlatna-vilitsa/ {
            proxy_pass http://zlatna_vilitsa/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        location /zlatna-vilitsa/webhooks/rest/webhook {
            proxy_pass http://zlatna_vilitsa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Хотел Гранд София
        location /grand-sofia/ {
            proxy_pass http://grand_sofia/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        location /grand-sofia/webhooks/rest/webhook {
            proxy_pass http://grand_sofia/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Медицински център Здраве+
        location /zdrave-medical/ {
            proxy_pass http://zdrave_medical/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        location /zdrave-medical/webhooks/rest/webhook {
            proxy_pass http://zdrave_medical/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_method POST;
        }
        
        # Автосервиз Мото Експерт
        location /moto-expert/ {
            proxy_pass http://moto_expert/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
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
        
        # Стартиране на контейнерите отново
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        # Тестване на API endpoints
        print("\n🧪 ТЕСТИРАНЕ НА API ENDPOINTS:")
        print("="*50)
        
        test_bots = [
            ('zlatna-kosa', 'Салон Златна коса'),
            ('zlatna-vilitsa', 'Ресторант Златна вилица'),
            ('grand-sofia', 'Хотел Гранд София'),
            ('zdrave-medical', 'Медицински център Здраве+'),
            ('moto-expert', 'Автосервиз Мото Експерт')
        ]
        
        for url_path, bot_name in test_bots:
            print(f"\n🤖 Тестване на {bot_name}...")
            
            # Тест на основния URL
            stdin, stdout, stderr = ssh.exec_command(f"curl -I http://localhost/{url_path}/")
            response = stdout.read().decode('utf-8')
            if "200 OK" in response:
                print(f"   ✅ Основен URL: OK")
            else:
                print(f"   ❌ Основен URL: {response[:100]}...")
            
            # Тест на API endpoint
            stdin, stdout, stderr = ssh.exec_command(f"curl -X POST http://localhost/{url_path}/webhooks/rest/webhook -H 'Content-Type: application/json' -d '{{\"message\": \"здравей\"}}'")
            api_response = stdout.read().decode('utf-8')
            
            if "405 Not Allowed" in api_response:
                print(f"   ❌ API: 405 Not Allowed")
            elif "error" in api_response.lower():
                print(f"   ❌ API: {api_response[:100]}...")
            else:
                print(f"   ✅ API: {api_response[:100]}...")
        
        print(f"\n🎉 Поправянето завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for url_path, bot_name in test_bots:
            print(f"   {bot_name}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    fix_nginx_api()
