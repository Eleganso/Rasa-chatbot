#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Direct Nginx Fix
Директен скрипт за поправяне на Nginx проблема
"""

import paramiko
import time

def fix_nginx_direct():
    """Директно поправя Nginx проблема"""
    print("🔧 ДИРЕКТНО ПОПРАВЯНЕ НА NGINX")
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
        
        # Спиране на всички контейнери
        print("\n🛑 Спиране на всички контейнери...")
        ssh.exec_command("cd /root/multi-bots && docker-compose down")
        time.sleep(5)
        
        # Създаване на нова Nginx конфигурация директно на VPS
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
        
        # Ресторант Златна вилица
        location /zlatna-vilitsa/ {
            proxy_pass http://zlatna_vilitsa/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        # Хотел Гранд София
        location /grand-sofia/ {
            proxy_pass http://grand_sofia/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        # Медицински център Здраве+
        location /zdrave-medical/ {
            proxy_pass http://zdrave_medical/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        # Автосервиз Мото Експерт
        location /moto-expert/ {
            proxy_pass http://moto_expert/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
        # DragonForged V2
        location /dragonforged-v2/ {
            proxy_pass http://dragonforged_v2/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
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
        
        # Проверка на статуса
        print("\n✅ Проверка на статуса...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Тестване на URL-ите
        print("\n🧪 Тестване на URL-ите...")
        test_urls = [
            "http://localhost/zlatna-kosa/",
            "http://localhost/zlatna-vilitsa/",
            "http://localhost/grand-sofia/",
            "http://localhost/zdrave-medical/",
            "http://localhost/moto-expert/"
        ]
        
        for url in test_urls:
            print(f"Тестване на {url}")
            stdin, stdout, stderr = ssh.exec_command(f"curl -I {url}")
            response = stdout.read().decode('utf-8')
            print(f"Отговор: {response[:100]}...")
        
        print("\n🎉 Поправянето завършено!")
        print("\n📋 Правилни URL-и:")
        print("   Салон 'Златна коса': http://37.60.225.86/zlatna-kosa/")
        print("   Ресторант 'Златна вилица': http://37.60.225.86/zlatna-vilitsa/")
        print("   Хотел 'Гранд София': http://37.60.225.86/grand-sofia/")
        print("   Медицински център 'Здраве+': http://37.60.225.86/zdrave-medical/")
        print("   Автосервиз 'Мото Експерт': http://37.60.225.86/moto-expert/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    fix_nginx_direct()
