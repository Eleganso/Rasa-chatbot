#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check VPS Structure
Проверка на структурата на VPS
"""

import paramiko

def check_vps_structure():
    """Проверява структурата на VPS"""
    print("🔍 ПРОВЕРКА НА СТРУКТУРАТА НА VPS")
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
        
        # Проверка на основната директория
        print("\n📁 Проверка на /root/multi-bots:")
        stdin, stdout, stderr = ssh.exec_command("ls -la /root/multi-bots/")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Проверка на bots директорията
        print("\n📁 Проверка на /root/multi-bots/bots:")
        stdin, stdout, stderr = ssh.exec_command("ls -la /root/multi-bots/bots/")
        output = stdout.read().decode('utf-8')
        print(output)
        
        # Проверка на всеки бот
        bots = ['zlatna_kosa', 'zlatna_vilitsa', 'grand_sofia', 'zdrave_medical', 'moto_expert']
        
        for bot in bots:
            print(f"\n📁 Проверка на /root/multi-bots/bots/{bot}:")
            stdin, stdout, stderr = ssh.exec_command(f"ls -la /root/multi-bots/bots/{bot}/")
            output = stdout.read().decode('utf-8')
            print(output)
            
            print(f"📁 Проверка на /root/multi-bots/bots/{bot}/web:")
            stdin, stdout, stderr = ssh.exec_command(f"ls -la /root/multi-bots/bots/{bot}/web/")
            output = stdout.read().decode('utf-8')
            print(output)
        
        ssh.close()
        return True
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
        return False

if __name__ == "__main__":
    check_vps_structure()
