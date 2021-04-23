class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f'Caught {pokemon.pokemon_details()}'
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for poke in self.pokemon:
            if pokemon_name == poke.pokemon_name:
                self.pokemon.remove(poke)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        pokemons_data = ''
        for poke in self.pokemon:
            pokemons_data += f'- {poke.pokemon_details()}\n'
        return f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n{pokemons_data}'
