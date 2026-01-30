# import requests

# api = "https://pokeapi.co/api/v2/"

# def get_pokemon(names):
#     pokemon_lists = []
#     for name in names:
#         url = f"{api}/pokemon/{name}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             pokemon_data = response.json()
#             pokemon_lists.append(pokemon_data)
#         else:
#             print(f"Failed to provieded {response.status_code}")
#     return pokemon_lists

# pokemons_names = ["pikachu", "typhlosion", "toto"]
# pokemons_info = get_pokemon(pokemons_names)

# if pokemons_info:
#     for pokemon_info in pokemons_info:
#         print(f"Name is {pokemon_info['name'].capitalize()}")
























import requests

api = "https://pokeapi.co/api/v2/"

def get_pokemon(names):
    pokemon_list = []
    for name in names:
        url = f"{api}/pokemon/{name}"
        response = requests.get(url)

        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon_list.append(pokemon_data)
        else:
            print(f"Failed data to recieved {response.status_code}")

    return pokemon_list
pokemon_names = ["pikachu", "typhlosion", "toto"]
pokemon_info = get_pokemon(pokemon_names)

if pokemon_info:
    for pokemons_info in pokemon_info:
        print(f"Name pokemon is {pokemons_info['name']}")