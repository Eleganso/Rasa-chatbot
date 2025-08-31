#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Multi-Bot Manager System
Управление на множество Rasa ботове едновременно
"""

import json
import os
import subprocess
import time
import sys
from datetime import datetime

class SimpleBotManager:
    def __init__(self):
        self.bots_file = "active_bots.json"
        self.active_bots = self.load_bots()
        self.processes = {}
        
    def load_bots(self):
        """Зарежда активните ботове от файл"""
        if os.path.exists(self.bots_file):
            try:
                with open(self.bots_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def save_bots(self):
        """Запазва активните ботове във файл"""
        with open(self.bots_file, 'w', encoding='utf-8') as f:
            json.dump(self.active_bots, f, indent=2, ensure_ascii=False)
    
    def add_bot(self, bot_name, bot_path, port, description=""):
        """Добавя нов бот"""
        if port in [bot['port'] for bot in self.active_bots.values()]:
            print(f"❌ Порт {port} вече се използва!")
            return False
            
        self.active_bots[bot_name] = {
            'path': bot_path,
            'port': port,
            'description': description,
            'status': 'stopped',
            'started_at': None,
            'pid': None,
            'url': f"http://localhost:{port}",
            'webhook_url': f"http://localhost:{port}/webhooks/rest/webhook"
        }
        self.save_bots()
        print(f"✅ Бот '{bot_name}' добавен успешно!")
        return True
    
    def remove_bot(self, bot_name):
        """Премахва бот"""
        if bot_name in self.active_bots:
            if self.active_bots[bot_name]['status'] == 'running':
                self.stop_bot(bot_name)
            del self.active_bots[bot_name]
            self.save_bots()
            print(f"✅ Бот '{bot_name}' премахнат!")
        else:
            print(f"❌ Бот '{bot_name}' не съществува!")
    
    def start_bot(self, bot_name):
        """Стартира бот"""
        if bot_name not in self.active_bots:
            print(f"❌ Бот '{bot_name}' не съществува!")
            return False
            
        bot = self.active_bots[bot_name]
        if bot['status'] == 'running':
            print(f"⚠️ Бот '{bot_name}' вече работи!")
            return True
            
        bot_path = bot['path']
        port = bot['port']
        
        if not os.path.exists(bot_path):
            print(f"❌ Пътят '{bot_path}' не съществува!")
            return False
        
        try:
            # Стартиране на Rasa сървъра
            cmd = [
                sys.executable, "-m", "rasa", "run",
                "--port", str(port),
                "--enable-api",
                "--cors", "*"
            ]
            
            process = subprocess.Popen(
                cmd,
                cwd=bot_path,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Изчакване малко за стартиране
            time.sleep(3)
            
            if process.poll() is None:  # Процесът все още работи
                bot['status'] = 'running'
                bot['pid'] = process.pid
                bot['started_at'] = datetime.now().isoformat()
                self.processes[bot_name] = process
                self.save_bots()
                print(f"✅ Бот '{bot_name}' стартиран на порт {port}!")
                return True
            else:
                print(f"❌ Грешка при стартиране на бот '{bot_name}'!")
                return False
                
        except Exception as e:
            print(f"❌ Грешка при стартиране на бот '{bot_name}': {e}")
            return False
    
    def stop_bot(self, bot_name):
        """Спира бот"""
        if bot_name not in self.active_bots:
            print(f"❌ Бот '{bot_name}' не съществува!")
            return False
            
        bot = self.active_bots[bot_name]
        if bot['status'] != 'running':
            print(f"⚠️ Бот '{bot_name}' не работи!")
            return True
        
        try:
            if bot_name in self.processes:
                process = self.processes[bot_name]
                process.terminate()
                process.wait(timeout=5)
                del self.processes[bot_name]
            
            bot['status'] = 'stopped'
            bot['pid'] = None
            bot['started_at'] = None
            self.save_bots()
            print(f"✅ Бот '{bot_name}' спрян!")
            return True
            
        except Exception as e:
            print(f"❌ Грешка при спиране на бот '{bot_name}': {e}")
            return False
    
    def restart_bot(self, bot_name):
        """Рестартира бот"""
        print(f"🔄 Рестартиране на бот '{bot_name}'...")
        self.stop_bot(bot_name)
        time.sleep(2)
        return self.start_bot(bot_name)
    
    def list_bots(self):
        """Показва списък с всички ботове"""
        if not self.active_bots:
            print("📝 Няма регистрирани ботове!")
            return
        
        print("\n" + "="*80)
        print("🤖 СПИСЪК С БОТОВЕ")
        print("="*80)
        
        for name, bot in self.active_bots.items():
            status_icon = "🟢" if bot['status'] == 'running' else "🔴"
            print(f"\n{status_icon} {name}")
            print(f"   📁 Път: {bot['path']}")
            print(f"   🌐 Порт: {bot['port']}")
            print(f"   📝 Описание: {bot['description']}")
            print(f"   🔗 URL: {bot['url']}")
            print(f"   🔗 Webhook: {bot['webhook_url']}")
            
            if bot['status'] == 'running':
                print(f"   ⏰ Стартиран: {bot['started_at']}")
                print(f"   🆔 PID: {bot['pid']}")
        
        print("\n" + "="*80)
    
    def start_all_bots(self):
        """Стартира всички ботове"""
        print("🚀 Стартиране на всички ботове...")
        for bot_name in self.active_bots.keys():
            self.start_bot(bot_name)
            time.sleep(2)
    
    def stop_all_bots(self):
        """Спира всички ботове"""
        print("🛑 Спиране на всички ботове...")
        for bot_name in list(self.active_bots.keys()):
            self.stop_bot(bot_name)

def main():
    manager = SimpleBotManager()
    
    # Добавяне на предварително конфигурирани ботове
    if not manager.active_bots:
        print("🔧 Инициализиране на ботове...")
        
        # DragonForged Dreams V2
        manager.add_bot(
            "dragonforged_v2",
            "bots/dragonforged_bot_v2/rasa",
            5005,
            "DragonForged Dreams Bot V2 - IT услуги и консултации"
        )
        
        # Салон Златна коса
        manager.add_bot(
            "zlatna_kosa",
            "bots/zlatna_kosa_salon/rasa",
            5006,
            "Салон 'Златна коса' - Красив салон и услуги"
        )
        
        # Ресторант Златна вилица
        manager.add_bot(
            "zlatna_vilitsa",
            "bots/zlatna_vilitsa_restaurant/rasa",
            5008,
            "Ресторант 'Златна вилица' - Автентични вкусове и топла атмосфера"
        )
        
        # Хотел Гранд София
        manager.add_bot(
            "grand_sofia",
            "bots/grand_sofia_hotel/rasa",
            5009,
            "Хотел 'Гранд София' - Луксозно гостоприемство в сърцето на столицата"
        )
        
        # Медицински център Здраве+
        manager.add_bot(
            "zdrave_medical",
            "bots/zdrave_medical_center/rasa",
            5010,
            "Медицински център 'Здраве+' - Вашето здраве е наш приоритет"
        )
        
        # Автосервиз Мото Експерт
        manager.add_bot(
            "moto_expert",
            "bots/moto_expert_autoservice/rasa",
            5011,
            "Автосервиз 'Мото Експерт' - Вашият надежден партньор за автомобилни услуги"
        )
        

    
    while True:
        print("\n" + "="*60)
        print("🤖 МУЛТИ-БОТ МЕНИДЖЪР")
        print("="*60)
        print("1. 📋 Списък с ботове")
        print("2. 🚀 Стартиране на бот")
        print("3. 🛑 Спиране на бот")
        print("4. 🔄 Рестартиране на бот")
        print("5. 🚀 Стартиране на всички")
        print("6. 🛑 Спиране на всички")
        print("7. ➕ Добавяне на нов бот")
        print("8. ➖ Премахване на бот")
        print("0. 🚪 Изход")
        print("="*60)
        
        choice = input("\nИзберете опция: ").strip()
        
        if choice == "1":
            manager.list_bots()
            
        elif choice == "2":
            manager.list_bots()
            bot_name = input("Въведете име на бота: ").strip()
            manager.start_bot(bot_name)
            
        elif choice == "3":
            manager.list_bots()
            bot_name = input("Въведете име на бота: ").strip()
            manager.stop_bot(bot_name)
            
        elif choice == "4":
            manager.list_bots()
            bot_name = input("Въведете име на бота: ").strip()
            manager.restart_bot(bot_name)
            
        elif choice == "5":
            manager.start_all_bots()
            
        elif choice == "6":
            manager.stop_all_bots()
            
        elif choice == "7":
            bot_name = input("Име на бота: ").strip()
            bot_path = input("Път до Rasa папката: ").strip()
            port = int(input("Порт: ").strip())
            description = input("Описание: ").strip()
            manager.add_bot(bot_name, bot_path, port, description)
            
        elif choice == "8":
            manager.list_bots()
            bot_name = input("Въведете име на бота: ").strip()
            manager.remove_bot(bot_name)
                
        elif choice == "0":
            print("🛑 Спиране на всички ботове...")
            manager.stop_all_bots()
            print("👋 Довиждане!")
            break
            
        else:
            print("❌ Невалидна опция!")
        
        input("\nНатиснете Enter за продължение...")

if __name__ == "__main__":
    main()
