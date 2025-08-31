#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check and Fix Nginx Configuration
Проверка и поправяне на Nginx конфигурацията
"""

import json
import paramiko
import time

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def check_and_fix_nginx():
    """Проверява и поправя Nginx конфигурацията"""
    print("🔧 ПРОВЕРКА И ПОПРАВЯНЕ НА NGINX")
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
        
        # Проверка на Nginx конфигурацията
        print("\n🌐 Проверка на Nginx конфигурацията...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && cat nginx.conf")
        nginx_config = stdout.read().decode('utf-8')
        print("Текуща Nginx конфигурация:")
        print(nginx_config)
        
        # Създаване на нова Nginx конфигурация
        print("\n🔧 Създаване на нова Nginx конфигурация...")
        new_nginx_config = create_correct_nginx_config(config)
        
        # Качване на новата конфигурация
        sftp = ssh.open_sftp()
        with open("nginx-fixed.conf", "w") as f:
            f.write(new_nginx_config)
        
        sftp.put("nginx-fixed.conf", "/root/multi-bots/nginx.conf")
        sftp.close()
        
        # Рестартиране на Nginx контейнера
        print("\n🔄 Рестартиране на Nginx контейнера...")
        ssh.exec_command("cd /root/multi-bots && docker-compose restart nginx")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(10)
        
        # Проверка на Nginx логовете
        print("\n📋 Проверка на Nginx логовете...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose logs nginx --tail=20")
        logs = stdout.read().decode('utf-8')
        print(logs)
        
        # Тестване на URL-ите
        print("\n🧪 Тестване на URL-ите...")
        for bot_id, bot_config in config['bots'].items():
            if bot_id != "dragonforged_v2":
                url_path = bot_id.replace("_", "-")
                test_url = f"http://localhost/{url_path}/"
                print(f"Тестване на {bot_config['name']}: {test_url}")
                
                stdin, stdout, stderr = ssh.exec_command(f"curl -I {test_url}")
                response = stdout.read().decode('utf-8')
                print(f"Отговор: {response[:200]}...")
        
        print("\n✅ Проверката завършена!")
        print("\n📋 Правилни URL-и:")
        for bot_id, bot_config in config['bots'].items():
            if bot_id != "dragonforged_v2":
                url_path = bot_id.replace("_", "-")
                print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

def create_correct_nginx_config(config):
    """Създава правилна Nginx конфигурация"""
    nginx_config = """events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    # Upstream блокове за всеки бот
"""
    
    # Добавяне на upstream блокове
    for bot_id, bot_config in config['bots'].items():
        nginx_config += f"""    upstream {bot_id} {{
        server {bot_id}:5005;
    }}
"""
    
    nginx_config += """
    server {
        listen 80;
        server_name 37.60.225.86;
        
        # Location блокове за всеки бот
"""
    
    # Добавяне на location блокове
    for bot_id, bot_config in config['bots'].items():
        url_path = bot_id.replace("_", "-")
        nginx_config += f"""        # {bot_config['name']}
        location /{url_path}/ {{
            proxy_pass http://{bot_id}/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_read_timeout 300;
            proxy_connect_timeout 300;
        }}
"""
    
    nginx_config += """
        # Статични файлове
        location / {
            root /var/www/html;
            index index.html;
            try_files $uri $uri/ =404;
        }
        
        # Health check
        location /health {
            return 200 "OK";
            add_header Content-Type text/plain;
        }
    }
}
"""
    
    return nginx_config

if __name__ == "__main__":
    check_and_fix_nginx()
