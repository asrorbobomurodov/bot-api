from settings import TOKEN
import requests

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

def send_message(chat_id: str, text: str):

    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(url, params=payload)

    return response.json()

send_message('6082673969', 'Wow')