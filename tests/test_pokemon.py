import requests
import pytest

token = '317e1aa9e1bc4e71aa931b9688a20690'
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 2573})
    assert response.status_code == 200

def test_name_trainer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 2573})
    assert response.json()['trainer_name'] == 'Алёна Н'

@pytest.mark.parametrize('key, value', [('name', 'Пряха'),
                                         ('trainer_id', '2573')])

def test_person_data(key, value) :
    response = requests.get(f'{host}/pokemons', params = {'trainer_id' : 2573})
    assert response.json()[0][key] == value