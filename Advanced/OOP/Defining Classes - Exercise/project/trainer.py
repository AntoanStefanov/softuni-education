class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon)
        return f'Caught {pokemon.pokemon_details()}'

    def release_pokemon(self, pokemon_name):
        for poke in self.pokemons:
            if poke.name == pokemon_name:
                self.pokemons.remove(poke)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        data = ''
        data += f"Pokemon Trainer {self.name}\n"
        caught_pokemons = len(self.pokemons)
        data += f"Pokemon count {caught_pokemons}"
        for poke in self.pokemons:
            data += f"\n- {poke.pokemon_details()}"
        return data


