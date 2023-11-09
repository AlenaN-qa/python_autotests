import requests
import json

token = '317e1aa9e1bc4e71aa931b9688a20690'
host = 'https://api.pokemonbattle.me:9104'

#создание покемона
response_new_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Пряха",
    "photo": "https://dolnikov.ru/pokemons/albums/187.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_new_pokemon.text)

# запись id покемона в переменную
new_pokemon = response_new_pokemon.json()['id'] 
print(new_pokemon)

#смена имени
response_new_name = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": new_pokemon,
    "name": "Сваха",
    "photo": "https://dolnikov.ru/pokemons/albums/187.png"
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_new_name.text)

#в покебол
response_in_pokebol = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": new_pokemon
}, headers = {'Content-Type' : 'application/json', 'trainer_token' : token})
print(response_in_pokebol.text)