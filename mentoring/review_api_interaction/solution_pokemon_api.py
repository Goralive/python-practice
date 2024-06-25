import requests

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(pokemon_name):
    response = requests.get(POKEMON_API_URL + pokemon_name)
    if response.status_code == 200:
        return response.json()
    else:
        raise PokemonNotFoundException("Meh, Something go wrong")


def parse_pokemon_details(pokemon_data):
    if not pokemon_data:
        return Exception("No data for pasing")
    details = {
        "name": pokemon_data["name"],
        "height": pokemon_data["height"],
        "weight": pokemon_data["weight"],
        "abilities": [
            ability["ability"]["name"] for ability in pokemon_data["abilities"]
        ],
    }
    return details


class PokemonNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)
