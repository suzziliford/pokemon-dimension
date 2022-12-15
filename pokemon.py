import requests

class Pokemon:
    def find_height_and_weight(self):
        name = "charizard"
        pokemon = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')  
        x = pokemon.json()
        print(f"{'pikachu'} weighs {x['weight']}")
        print(f"{'pickachu'} has a height of {x['height']} thingies")
    


a = Pokemon()
a.find_height_and_weight()

