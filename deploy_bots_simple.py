#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Bot Deployment Script
Опростен скрипт за деплойване на ботове на VPS
"""

import json
import os
import paramiko
import time
from datetime import datetime

def load_config():
    """Зарежда конфигурацията"""
    with open('bots_config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def deploy_bots():
    """Деплойва ботовете на VPS"""
    print("🤖 ДЕПЛОЙВАНЕ НА БОТОВЕ НА VPS")
    print("="*50)
    
    # Зареждане на конфигурацията
    config = load_config()
    
    # VPS данни
    host = "37.60.225.86"
    username = input("Потребителско име (root): ").strip() or "root"
    password = input("Парола: ").strip()
    
    print(f"\n🚀 Свързване с {host}...")
    
    try:
        # Свързване с VPS
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)
        print("✅ Успешно свързване!")
        
        # Създаване на директории
        print("\n📁 Създаване на директории...")
        ssh.exec_command("mkdir -p /root/multi-bots")
        ssh.exec_command("mkdir -p /root/multi-bots/web_interfaces")
        
        # Качване на ботовете
        print("\n📤 Качване на ботове...")
        sftp = ssh.open_sftp()
        
        for bot_id, bot_config in config['bots'].items():
            if bot_id == "dragonforged_v2":
                print(f"⏭️  Пропускане на {bot_id} (вече е качен)")
                continue
                
            print(f"📤 Качване на {bot_id}...")
            
            # Създаване на директория за бота
            remote_dir = f"/root/multi-bots/{bot_config['path']}"
            ssh.exec_command(f"mkdir -p {remote_dir}")
            
            # Качване на Rasa файлове
            local_rasa_path = bot_config['path']
            if os.path.exists(local_rasa_path):
                for file in os.listdir(local_rasa_path):
                    local_file = os.path.join(local_rasa_path, file)
                    if os.path.isfile(local_file):
                        remote_file = f"{remote_dir}/{file}"
                        sftp.put(local_file, remote_file)
                        print(f"   ✅ {file}")
            
            # Качване на уеб интерфейса
            web_interface = bot_config['web_interface']
            if os.path.exists(web_interface):
                remote_web = f"/root/multi-bots/web_interfaces/{bot_id}.html"
                sftp.put(web_interface, remote_web)
                print(f"   ✅ web interface")
        
        sftp.close()
        
        # Създаване на docker-compose.yml
        print("\n🐳 Създаване на Docker Compose...")
        compose_content = create_docker_compose(config)
        with open("docker-compose-multi.yml", "w") as f:
            f.write(compose_content)
        
        sftp = ssh.open_sftp()
        sftp.put("docker-compose-multi.yml", "/root/multi-bots/docker-compose.yml")
        sftp.close()
        
        # Създаване на Nginx конфигурация
        print("🌐 Създаване на Nginx конфигурация...")
        nginx_content = create_nginx_config(config)
        with open("nginx-multi.conf", "w") as f:
            f.write(nginx_content)
        
        sftp = ssh.open_sftp()
        sftp.put("nginx-multi.conf", "/root/multi-bots/nginx.conf")
        sftp.close()
        
        # Стартиране на Docker Compose
        print("\n🚀 Стартиране на Docker Compose...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране на контейнерите...")
        time.sleep(15)
        
        # Проверка на статуса
        print("\n✅ Проверка на статуса...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
        print("\n🎉 Деплойването завършено успешно!")
        print("\n📋 Достъпни URL-и:")
        for bot_id, bot_config in config['bots'].items():
            if bot_id != "dragonforged_v2":
                url_path = bot_id.replace("_", "-")
                print(f"   {bot_config['name']}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка при деплойване: {e}")
        return False

def create_docker_compose(config):
    """Създава docker-compose.yml"""
    compose_content = """version: '3.8'

services:
"""
    
    # Добавяне на ботовете
    for bot_id, bot_config in config['bots'].items():
        compose_content += f"""
  {bot_id}:
    image: rasa/rasa:3.6.21
    container_name: {bot_id}
    ports:
      - "{bot_config['port']}:5005"
    volumes:
      - ./{bot_config['path']}:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network
"""
    
    # Добавяне на Nginx
    compose_content += """
  nginx:
    image: nginx:alpine
    container_name: multi-bot-nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - ./web_interfaces:/var/www/html
    depends_on:
"""
    
    for bot_id in config['bots'].keys():
        compose_content += f"      - {bot_id}\n"
    
    compose_content += """    restart: unless-stopped
    networks:
      - bot-network

networks:
  bot-network:
    driver: bridge
"""
    
    return compose_content

def create_nginx_config(config):
    """Създава Nginx конфигурация"""
    nginx_config = """events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
"""
    
    # Добавяне на upstream блокове
    for bot_id, bot_config in config['bots'].items():
        nginx_config += f"""
    upstream {bot_id} {{
        server {bot_id}:{bot_config['port']};
    }}
"""
    
    nginx_config += """
    
    server {
        listen 80;
        server_name 37.60.225.86;
"""
    
    # Добавяне на location блокове
    for bot_id, bot_config in config['bots'].items():
        url_path = bot_id.replace("_", "-")
        nginx_config += f"""
        # {bot_config['name']}
        location /{url_path}/ {{
            proxy_pass http://{bot_id}/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }}
"""
    
    nginx_config += """
        # Статични файлове
        location / {
            root /var/www/html;
            index index.html;
            try_files $uri $uri/ =404;
        }
    }
}
"""
    
    return nginx_config

if __name__ == "__main__":
    deploy_bots()
