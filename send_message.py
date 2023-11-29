from settings import TOKEN
import requests

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def send_message(chat_id, text):
    payload = {
        "chat_id": chat_id,
        "text": text,
    }
    requests.get(url, params=payload)

send_message('1258594598', 'hi')
