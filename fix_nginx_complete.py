import paramiko
import time

def fix_nginx_config():
    # SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        ssh.connect('37.60.225.86', username='root', password='Contabo2024!')
        
        # Създаваме нов nginx.conf с правилно форматиране
        nginx_config = """events {
    worker_connections 1024;
}

http {
    upstream zlatna_kosa {
        server zlatna_kosa_salon:5005;
    }
    
    upstream zlatna_vilitsa {
        server zlatna_vilitsa_restaurant:5005;
    }
    
    upstream grand_sofia {
        server grand_sofia_hotel:5005;
    }
    
    upstream zdravet_plus {
        server zdravet_plus_medical:5005;
    }
    
    upstream moto_expert {
        server moto_expert_auto:5005;
    }

    server {
        listen 80;
        server_name 37.60.225.86;

        # Салон Златна коса - статичен файл
        location /zlatna-kosa/ {
            alias /var/www/bots/zlatna_kosa_salon/web/;
            default_type text/html;
            try_files $uri $uri/ /index.html;
        }

        location /zlatna-kosa/webhooks/rest/webhook {
            proxy_pass http://zlatna_kosa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Ресторант Златна вилица - статичен файл
        location /zlatna-vilitsa/ {
            alias /var/www/bots/zlatna_vilitsa_restaurant/web/;
            default_type text/html;
            try_files $uri $uri/ /index.html;
        }

        location /zlatna-vilitsa/webhooks/rest/webhook {
            proxy_pass http://zlatna_vilitsa/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Хотел Гранд София - статичен файл
        location /grand-sofia/ {
            alias /var/www/bots/grand_sofia_hotel/web/;
            default_type text/html;
            try_files $uri $uri/ /index.html;
        }

        location /grand-sofia/webhooks/rest/webhook {
            proxy_pass http://grand_sofia/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Медицински център Здраве+ - статичен файл
        location /zdravet-plus/ {
            alias /var/www/bots/zdravet_plus_medical/web/;
            default_type text/html;
            try_files $uri $uri/ /index.html;
        }

        location /zdravet-plus/webhooks/rest/webhook {
            proxy_pass http://zdravet_plus/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Автосервиз Мото Експерт - статичен файл
        location /moto-expert/ {
            alias /var/www/bots/moto_expert_auto/web/;
            default_type text/html;
            try_files $uri $uri/ /index.html;
        }

        location /moto-expert/webhooks/rest/webhook {
            proxy_pass http://moto_expert/webhooks/rest/webhook;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}"""
        
        # Записваме новия конфиг
        sftp = ssh.open_sftp()
        with sftp.file('/root/multi-bots/nginx.conf', 'w') as f:
            f.write(nginx_config)
        sftp.close()
        
        print("✅ nginx.conf презаписан успешно")
        
        # Рестартираме nginx контейнера
        print("🔄 Рестартиране на nginx контейнера...")
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose restart nginx")
        time.sleep(5)
        
        # Проверяваме статуса
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose ps nginx")
        status = stdout.read().decode('utf-8')
        print(f"Статус на nginx: {status}")
        
        # Проверяваме логовете
        stdin, stdout, stderr = ssh.exec_command("cd /root/multi-bots && docker-compose logs --tail=10 nginx")
        logs = stdout.read().decode('utf-8')
        print(f"Логове на nginx:\n{logs}")
        
    except Exception as e:
        print(f"❌ Грешка: {e}")
    finally:
        ssh.close()

if __name__ == "__main__":
    fix_nginx_config()
