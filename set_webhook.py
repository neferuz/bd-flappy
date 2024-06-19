import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
WEBHOOK_URL = "https://yourdomain.com/webhook"  # Замени на URL твоего сервера

set_webhook_url = f"https://api.telegram.org/bot{TOKEN}/setWebhook?url={WEBHOOK_URL}"
response = requests.get(set_webhook_url)
print(response.json())