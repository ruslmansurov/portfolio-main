# import requests

# base_url = "https://pokeapi.co/api/v2/"


# def get_pokemon(name):
#     url = f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     print(response)

#     if response.status_code == 200:
#        pokemon_data = response.json()
#        return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "pikachu"
# pokemon_info = get_pokemon(pokemon_name)

# if pokemon_info:
#     print(f"{pokemon_info["name"]}")

# import requests

# base_url = "https://pokeapi.co/api/v2/"


# def get_pokemon(names):
#     pokimon_list = []
#     for name in names:
#         url = f"{base_url}/pokemon/{name}"
#         response = requests.get(url)

#         if response.status_code == 200:
#             pokemon_data = response.json()
#             pokimon_list.append(pokemon_data)
#         else:
#             print(f"Failed to retrived data {response.status_code}")
#     return pokimon_list

# pokemon_name = ["pikachu", "typhlosion"]
# pokemon_info = get_pokemon(pokemon_name)

# if pokemon_info:
#     for pokemons_info in pokemon_info:
#         print(f"{pokemons_info['name'].capitalize()}")






# import requests

# base_url = "https://pokeapi.co/api/v2/"

# def get_pokemon(names):
#     pokemon_list = []
#     for name in names:
#         url = f"{base_url}/pokemon/{name}"
#         response = requests.get(url)
#         pokemon_data = response.json()
#         pokemon_list.append(pokemon_data)
#     return pokemon_list

# pokemon_names = ["pikachu", "typhlosion"]
# pokemon_info = get_pokemon(pokemon_names)

# if pokemon_info:
#     for pokemons_info in pokemon_info:
#         print(f"Name is {pokemons_info['name'].capitalize()}")


#         # if pokemon_info:
# #     for pokemons_info in pokemon_info:
# #         print(f"{pokemons_info['name'].capitalize()}")



from cat import Cat
from dog import Dog


cat_1 = Cat("Garfield", 5)
print(cat_1.name, cat_1.age, cat_1.gender)
cat_1.talk()
cat_2 = Cat("Murka", 3)
print(cat_2.name, cat_2.age, cat_2.gender)
cat_2.talk()


dog_1 = Dog("Tayson", 2, "Chihuahua")
dog_1.talk()
dog_1.run()