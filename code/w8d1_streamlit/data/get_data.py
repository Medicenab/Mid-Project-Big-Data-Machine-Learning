import re
import requests
def get_all_pokemon(numero):
    return requests.get(f"http://127.0.0.1:8000/range/pokemons/{numero}").json()



