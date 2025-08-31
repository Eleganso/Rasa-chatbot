#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create New Docker Compose
Създаване на нов Docker Compose файл
"""

import paramiko
import time

def create_new_docker_compose():
    """Създава нов Docker Compose файл"""
    print("📝 СЪЗДАВАНЕ НА НОВ DOCKER COMPOSE ФАЙЛ")
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
        
        # Създаване на нов Docker Compose файл
        print("\n📝 Създаване на нов Docker Compose файл...")
        
        docker_compose = """version: '3.8'

services:
  zlatna_kosa:
    image: rasa/rasa:3.6.21
    container_name: zlatna_kosa
    ports:
      - "5006:5005"
    volumes:
      - ./bots/zlatna_kosa_salon/rasa:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network

  zlatna_vilitsa:
    image: rasa/rasa:3.6.21
    container_name: zlatna_vilitsa
    ports:
      - "5008:5005"
    volumes:
      - ./bots/zlatna_vilitsa_restaurant/rasa:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network

  grand_sofia:
    image: rasa/rasa:3.6.21
    container_name: grand_sofia
    ports:
      - "5009:5005"
    volumes:
      - ./bots/grand_sofia_hotel/rasa:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network

  zdrave_medical:
    image: rasa/rasa:3.6.21
    container_name: zdrave_medical
    ports:
      - "5010:5005"
    volumes:
      - ./bots/zdrave_medical_center/rasa:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network

  moto_expert:
    image: rasa/rasa:3.6.21
    container_name: moto_expert
    ports:
      - "5011:5005"
    volumes:
      - ./bots/moto_expert_autoservice/rasa:/app
    working_dir: /app
    command: run --enable-api --cors "*" --port 5005
    restart: unless-stopped
    networks:
      - bot-network

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
      - zlatna_kosa
      - zlatna_vilitsa
      - grand_sofia
      - zdrave_medical
      - moto_expert
    restart: unless-stopped
    networks:
      - bot-network

networks:
  bot-network:
    driver: bridge
"""
        
        # Записване на новия файл
        ssh.exec_command("cd /root/multi-bots && echo '" + docker_compose.replace("'", "'\"'\"'") + "' > docker-compose.yml")
        
        # Стартиране на контейнерите
        print("\n🚀 Стартиране на контейнерите...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        
        # Изчакване за стартиране
        print("⏳ Изчакване за стартиране...")
        time.sleep(20)
        
        # Проверка на статуса
        print("\n📊 Статус на контейнерите:")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        output = stdout.read().decode('utf-8')
        print(output)
        
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
        
        print(f"\n🎉 Създаването завършено!")
        print(f"\n🌐 URL-и за тестване:")
        for url_path, bot_name in test_urls:
            print(f"   {bot_name}: http://{host}/{url_path}/")
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    create_new_docker_compose()
