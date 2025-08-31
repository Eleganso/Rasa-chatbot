#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-Bot VPS Deployment Script
Скрипт за деплойване на множество ботове на VPS
"""

import json
import os
import subprocess
import paramiko
import time
from datetime import datetime

class MultiBotDeployer:
    def __init__(self, config_file="bots_config.json"):
        self.config = self.load_config(config_file)
        self.ssh_client = None
        
    def load_config(self, config_file):
        """Зарежда конфигурацията"""
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def connect_ssh(self, host, username, password):
        """Свързване с VPS"""
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(host, username=username, password=password)
            print(f"✅ Успешно свързване с {host}")
            return True
        except Exception as e:
            print(f"❌ Грешка при свързване: {e}")
            return False
    
    def execute_command(self, command):
        """Изпълнява команда на VPS"""
        if not self.ssh_client:
            print("❌ Няма активна SSH връзка!")
            return None
            
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            output = stdout.read().decode('utf-8')
            error = stderr.read().decode('utf-8')
            return output, error
        except Exception as e:
            print(f"❌ Грешка при изпълнение на команда: {e}")
            return None, str(e)
    
    def upload_file(self, local_path, remote_path):
        """Качва файл на VPS"""
        if not self.ssh_client:
            print("❌ Няма активна SSH връзка!")
            return False
            
        try:
            sftp = self.ssh_client.open_sftp()
            sftp.put(local_path, remote_path)
            sftp.close()
            print(f"✅ Файл качен: {local_path} -> {remote_path}")
            return True
        except Exception as e:
            print(f"❌ Грешка при качване на файл: {e}")
            return False
    
    def create_docker_compose(self):
        """Създава docker-compose.yml за всички ботове"""
        compose_content = """version: '3.8'

services:
"""
        
        # Добавяне на ботовете
        for bot_id, bot_config in self.config['bots'].items():
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
        
        for bot_id in self.config['bots'].keys():
            compose_content += f"      - {bot_id}\n"
        
        compose_content += """    restart: unless-stopped
    networks:
      - bot-network

networks:
  bot-network:
    driver: bridge
"""
        
        return compose_content
    
    def create_nginx_config(self):
        """Създава Nginx конфигурация"""
        nginx_config = """events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    
    upstream dragonforged_v2 {
        server dragonforged_v2:5005;
    }
    
    upstream zlatna_kosa {
        server zlatna_kosa:5006;
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
    

    
    server {
        listen 80;
        server_name 37.60.225.86;
        
        # DragonForged Dreams V2
        location /dragonforged-v2/ {
            proxy_pass http://dragonforged_v2/;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
        
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
    
    def deploy_to_vps(self, host, username, password):
        """Деплойва всички ботове на VPS"""
        print("🚀 Стартиране на деплойване на VPS...")
        
        # Свързване с VPS
        if not self.connect_ssh(host, username, password):
            return False
        
        try:
            # Създаване на директории
            print("📁 Създаване на директории...")
            self.execute_command("mkdir -p /root/multi-bots")
            self.execute_command("mkdir -p /root/multi-bots/web_interfaces")
            
            # Качване на ботовете
            print("📤 Качване на ботове...")
            for bot_id, bot_config in self.config['bots'].items():
                local_path = bot_config['path']
                remote_path = f"/root/multi-bots/{bot_config['path']}"
                
                # Създаване на директория
                self.execute_command(f"mkdir -p /root/multi-bots/{os.path.dirname(bot_config['path'])}")
                
                # Качване на файлове
                if os.path.exists(local_path):
                    self.upload_file(local_path, remote_path)
            
            # Качване на уеб интерфейси
            print("🌐 Качване на уеб интерфейси...")
            for bot_id, bot_config in self.config['bots'].items():
                web_interface = bot_config['web_interface']
                if os.path.exists(web_interface):
                    remote_web = f"/root/multi-bots/web_interfaces/{bot_id}.html"
                    self.upload_file(web_interface, remote_web)
            
            # Създаване на docker-compose.yml
            print("🐳 Създаване на Docker Compose...")
            compose_content = self.create_docker_compose()
            with open("docker-compose-multi.yml", "w") as f:
                f.write(compose_content)
            
            self.upload_file("docker-compose-multi.yml", "/root/multi-bots/docker-compose.yml")
            
            # Създаване на Nginx конфигурация
            print("🌐 Създаване на Nginx конфигурация...")
            nginx_content = self.create_nginx_config()
            with open("nginx-multi.conf", "w") as f:
                f.write(nginx_content)
            
            self.upload_file("nginx-multi.conf", "/root/multi-bots/nginx.conf")
            
            # Стартиране на Docker Compose
            print("🚀 Стартиране на Docker Compose...")
            self.execute_command("cd /root/multi-bots && docker-compose up -d")
            
            # Проверка на статуса
            print("✅ Проверка на статуса...")
            time.sleep(10)
            output, error = self.execute_command("cd /root/multi-bots && docker-compose ps")
            print(output)
            
            print("\n🎉 Деплойването завършено успешно!")
            print("\n📋 Достъпни URL-и:")
            for bot_id, bot_config in self.config['bots'].items():
                print(f"   {bot_config['name']}: http://{host}/dragonforged-v2/")
            
            return True
            
        except Exception as e:
            print(f"❌ Грешка при деплойване: {e}")
            return False
        finally:
            if self.ssh_client:
                self.ssh_client.close()

def main():
    print("🤖 МУЛТИ-БОТ VPS ДЕПЛОЙЕР")
    print("="*50)
    
    deployer = MultiBotDeployer()
    
    # Въвеждане на VPS данни
    host = input("VPS IP адрес: ").strip()
    username = input("Потребителско име: ").strip()
    password = input("Парола: ").strip()
    
    # Деплойване
    deployer.deploy_to_vps(host, username, password)

if __name__ == "__main__":
    main()
