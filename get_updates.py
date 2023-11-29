from settings import TOKEN
import requests

url = f'https://api.telegram.org/bot{TOKEN}/getUpdates'

def get_updates():
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()['result']
    else:
        return False


def get_last_update(updates: list[dict]) -> dict:
    return updates[-1]

updates = get_updates()
last_update = get_last_update(updates)
print(last_update)
