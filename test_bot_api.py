import requests
import json

def test_bot_api():
    # Тестваме API endpoint директно
    url = "http://37.60.225.86/zlatna-kosa/webhooks/rest/webhook"
    data = {
        "message": "здравей",
        "sender": "test_user"
    }
    
    try:
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'})
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_bot_api()
