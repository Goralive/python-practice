import unittest

from solution_pokemon_api import (
    get_pokemon_data,
    PokemonNotFoundException,
    parse_pokemon_details,
)


class TestPokemonAPI(unittest.TestCase):
    def test_get_pokemon_data(self):
        pika = "pikachu"
        data = get_pokemon_data(pika)
        self.assertIsNotNone(data)
        self.assertEqual(data["name"], pika)

    def test_get_invalid_pokemon(self):
        with self.assertRaises(PokemonNotFoundException):
            get_pokemon_data("Jackson Ford")

    def test_parse_pokemon_details(self):
        sample_data = {
            "name": "pikachu",
            "height": 4,
            "weight": 60,
            "abilities": [
                {"ability": {"name": "static"}},
                {"ability": {"name": "lightning-rod"}},
            ],
        }
        expected_details = {
            "name": "pikachu",
            "height": 4,
            "weight": 60,
            "abilities": ["static", "lightning-rod"],
        }
        details = parse_pokemon_details(sample_data)
        self.assertEqual(details, expected_details)

        parse_pokemon_details(None)
        self.assertIsNone(details)
