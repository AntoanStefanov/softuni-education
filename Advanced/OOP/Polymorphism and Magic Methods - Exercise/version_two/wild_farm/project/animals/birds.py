from .animal import Bird
from ..food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):
    INCREASE_WEIGHT_PER_PIECE = 0.25
    ONLY_FOOD_EATING = (Meat,)

    @staticmethod
    def make_sound(): return 'Hoot Hoot'


class Hen(Bird):
    INCREASE_WEIGHT_PER_PIECE = 0.35
    ONLY_FOOD_EATING = None #(Meat, Vegetable, Seed, Fruit)

    @staticmethod
    def make_sound(): return 'Cluck'
