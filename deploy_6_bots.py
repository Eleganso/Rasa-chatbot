import paramiko
import os
import time

def deploy_6_bots():
    # SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect('37.60.225.86', username='root', password='Contabo2024!')
        
        print("🚀 Стартиране на deployment на 6 бота...")
        
        # Създаваме директорията
        print("📁 Създаване на директории...")
        ssh.exec_command("mkdir -p /root/multi-bots")
        time.sleep(2)
        
        # Качваме docker-compose.yml
        print("📄 Качване на docker-compose.yml...")
        sftp = ssh.open_sftp()
        sftp.put('docker-compose.yml', '/root/multi-bots/docker-compose.yml')
        
        # Качваме nginx.conf
        print("📄 Качване на nginx.conf...")
        sftp.put('nginx.conf', '/root/multi-bots/nginx.conf')
        sftp.close()
        
        # Създаваме структурата на директориите
        print("📁 Създаване на структура на директориите...")
        bot_dirs = [
            'dragonforged_bot_v2',
            'zlatna_kosa_salon', 
            'zlatna_vilitsa_restaurant',
            'grand_sofia_hotel',
            'zdravet_plus_medical',
            'moto_expert_auto'
        ]
        
        for bot_dir in bot_dirs:
            ssh.exec_command(f"mkdir -p /root/multi-bots/bots/{bot_dir}/rasa")
            ssh.exec_command(f"mkdir -p /root/multi-bots/bots/{bot_dir}/web")
        
        # Копираме съществуващите ботове
        print("📋 Копиране на съществуващи ботове...")
        
        # DragonForged Bot V2
        if os.path.exists('bots/dragonforged_bot_v2'):
            print("🐉 Копиране на DragonForged Bot V2...")
            ssh.exec_command("cp -r /root/bots/dragonforged_bot_v2/rasa/* /root/multi-bots/bots/dragonforged_bot_v2/rasa/")
            ssh.exec_command("cp -r /root/bots/dragonforged_bot_v2/web/* /root/multi-bots/bots/dragonforged_bot_v2/web/")
        
        # Копираме новите ботове
        new_bots = {
            'zlatna_kosa_salon': 'Салон "Златна коса"',
            'zlatna_vilitsa_restaurant': 'Ресторант "Златна вилица"',
            'grand_sofia_hotel': 'Хотел "Гранд София"',
            'zdravet_plus_medical': 'Медицински център "Здраве+"',
            'moto_expert_auto': 'Автосервиз "Мото Експерт"'
        }
        
        for bot_dir, bot_name in new_bots.items():
            if os.path.exists(f'bots/{bot_dir}'):
                print(f"📋 Копиране на {bot_name}...")
                ssh.exec_command(f"cp -r /root/bots/{bot_dir}/rasa/* /root/multi-bots/bots/{bot_dir}/rasa/")
                ssh.exec_command(f"cp -r /root/bots/{bot_dir}/web/* /root/multi-bots/bots/{bot_dir}/web/")
        
        # Стартираме контейнерите
        print("🐳 Стартиране на Docker контейнери...")
        ssh.exec_command("cd /root/multi-bots && docker-compose up -d")
        time.sleep(10)
        
        # Проверяваме статуса
        print("✅ Проверка на статуса...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps")
        status = stdout.read().decode('utf-8')
        print(f"Статус на контейнерите:\n{status}")
        
        print("🎉 Deployment завършен успешно!")
        print("\n🌐 Достъпни ботове:")
        print("• DragonForged Bot V2: http://37.60.225.86/dragonforged/")
        print("• Салон Златна коса: http://37.60.225.86/zlatna-kosa/")
        print("• Ресторант Златна вилица: http://37.60.225.86/zlatna-vilitsa/")
        print("• Хотел Гранд София: http://37.60.225.86/grand-sofia/")
        print("• Медицински център Здраве+: http://37.60.225.86/zdravet-plus/")
        print("• Автосервиз Мото Експерт: http://37.60.225.86/moto-expert/")
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    deploy_6_bots()
