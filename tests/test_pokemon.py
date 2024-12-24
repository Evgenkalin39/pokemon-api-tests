import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8ef51db57802ffbf033ce7a686174dd9'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}
TRAINER_ID = 13585
def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
    print(f"\nURL запроса: {response.url}")
    print(f"Статус код: {response.status_code}")
    print(f"Тело ответа: {response.json()}")
    print(f"Заголовки ответа: {response.headers}")
    print(f"Время выполнения: {response.elapsed.total_seconds()} сек")
    assert response.status_code == 200

def test_trainer_name():
   response = requests.get(url=f'{URL}/trainers', params={'trainer_id': TRAINER_ID})
   trainer_name = response.json()['data'][0]['trainer_name']
   print(f"\nИмя тренера в ответе: {trainer_name}")
   assert trainer_name == "Evgen"