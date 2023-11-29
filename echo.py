from settings import TOKEN
from get_updates import get_updates
import requests
from time import sleep



def echo(chat_id: str, text: str):

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': text
    }

    response = requests.get(url, params=payload)

    return response.json()



last_update_id = -1

while True:
    updates = get_updates()[-1]

    if updates['update_id'] != last_update_id:
        data = updates['message']
        chat_id = data['chat']['id']
        t = data['text']

        last_update_id = updates['update_id']
        echo(chat_id, t)

    sleep(0.5)

