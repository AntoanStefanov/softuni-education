class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, animal):
        animals = ''
        if species == "mammal":
            animals = self.mammals
        elif species == "fish":
            animals = self.fishes
        elif species == "bird":
            animals = self.birds
        Zoo.__animals += 1
        animals.append(animal)

    def get_info(self, species):
        info = ''
        if species == "mammal":
            info += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            info += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            info += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"
        info += f"Total animals: {Zoo.__animals}"
        return info


zoo_name = input()
zoo = Zoo(zoo_name)
animals_to_add = int(input())

for _ in range(animals_to_add):
    species, animal = input().split()
    zoo.add_animal(species, animal)

info = input()

print(zoo.get_info(info))
