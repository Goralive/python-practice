import requests

POKEMON_API_URL = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_data(pokemon_name):
    response = requests.get(POKEMON_API_URL + pokemon_name)
    print(response.json())
    return True


def parse_pokemon_details(pokemon_data):

    pass


class PokemonNotFoundException(Exception):
    pass


try:
    pokemon_data = get_pokemon_data("pikachu")
    parsed_details = parse_pokemon_details(pokemon_data)
    print(parsed_details)
except PokemonNotFoundException as e:
    print(e)
