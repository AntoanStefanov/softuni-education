from .animal import Mammal
from ..food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    INCREASE_WEIGHT_PER_PIECE = 0.10
    ONLY_FOOD_EATING = (Fruit, Vegetable)

    @staticmethod
    def make_sound(): return 'Squeak'


class Dog(Mammal):
    INCREASE_WEIGHT_PER_PIECE = 0.40
    ONLY_FOOD_EATING = (Meat,)

    @staticmethod
    def make_sound(): return 'Woof!'


class Cat(Mammal):
    INCREASE_WEIGHT_PER_PIECE = 0.30
    ONLY_FOOD_EATING = (Meat, Vegetable)

    @staticmethod
    def make_sound(): return 'Meow'


class Tiger(Mammal):
    INCREASE_WEIGHT_PER_PIECE = 1.00
    ONLY_FOOD_EATING = (Meat,)

    @staticmethod
    def make_sound(): return 'ROAR!!!'
