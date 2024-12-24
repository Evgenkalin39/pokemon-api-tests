import  requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8ef51db57802ffbf033ce7a686174dd9'
HEADER = {'Content-Type': 'application/json','trainer_token': TOKEN}

Body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
Body_menyaem_imya = {
    "pokemon_id": "168503",
    "name": "New Name",
    "photo_id": -1
}
''''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = Body_create_pokemon )
print(response_create.status_code)  # код ответа
print(response_create.json())   # тело ответа

pokemons_id = response_create.json()['id']'''

'''response_menyaem_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = Body_menyaem_imya )
print(response_menyaem_name.status_code)  # код ответа
print(response_menyaem_name.json())    # тело ответа'''

body_pokeball = {
    "pokemon_id": "168503"
}

response_lovim_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball )
print(response_lovim_pokeball.status_code)  # код ответа
print(response_lovim_pokeball.json())    # тело ответа

