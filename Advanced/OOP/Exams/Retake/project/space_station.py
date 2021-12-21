from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut:
            return f"{name} is already added."
        if astronaut_type == 'Biologist' or astronaut_type == 'Geodesist' or astronaut_type == 'Meteorologist':
            if astronaut_type == 'Biologist':
                astro = Biologist(name)
                self.astronaut_repository.add(astro)
            elif astronaut_type == 'Geodesist':
                astro = Geodesist(name)
                self.astronaut_repository.add(astro)
            elif astronaut_type == 'Meteorologist':
                astro = Meteorologist(name)
                self.astronaut_repository.add(astro)

            return f"Successfully added {astronaut_type}: {name}."

        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str):
        planet = self.planet_repository.find_by_name(name)
        if planet:
            return f"{name} is already added."
        planet = Planet(name)
        items = items.split(', ')
        planet.items.extend(items)
        self.planet_repository.add(planet)
        return f"{name} is already added."

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exists!")
        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")
        suitable_astronauts = [astronaut for astronaut in self.astronaut_repository.astronauts if astronaut.oxygen > 30]
        if not suitable_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

    def report(self):
        pass
