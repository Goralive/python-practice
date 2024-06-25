## Pokemon API

URL = https://pokeapi.co/

1. Install and import requests to you
2. Implements methods to get and parse pokemon (name, height, weight, ability.name)
3. Test should be passing
4. Handle errors

Optional tasks:

- Add loging
- Filter Pokemons with ability.name *lightning-rod*
- Save name of the Pokemon that have ability *lightning-rod* to file (.txt, .csv)

<details>
<summary>Click to reveal instructions</summary>

Step-by-Step Guide to Implementing Pokémon API Interaction
1. Import Necessary Module:

- Begin by importing the requests module in your Python script. This module will be used to make HTTP requests to the Pokémon API.
2. Define Constants:

- Define a constant variable to hold the base URL of the Pokémon API. This will be used to construct the complete URL for fetching Pokémon data.
3. Create Function to Get Pokémon Data:

- Define a function, let's call it get_pokemon_data, that takes the name of a Pokémon as input.
- Inside this function, construct the complete URL by appending the Pokémon name to the base URL.
- Use the requests.get() function to make a GET request to the constructed URL.
- Check the status code of the response. If it's 200, return the JSON data from the response. Otherwise, raise a custom exception (e.g., PokemonNotFoundException) to indicate that the Pokémon was not found.
4. Create Function to Parse Pokémon Details:

- Define a function, perhaps named parse_pokemon_details, that takes the Pokémon data (JSON) as input.
- Extract relevant details from the Pokémon data, such as name, height, weight, and abilities.
- Return these details in a structured format, such as a dictionary.
5. Define Custom Exception:

- Define a custom exception class, such as PokemonNotFoundException, to handle cases where a Pokémon is not found.
- This exception class can inherit from the base Exception class.

</details>
