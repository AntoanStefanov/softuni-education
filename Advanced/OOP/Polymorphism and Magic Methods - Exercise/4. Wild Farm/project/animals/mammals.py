from .animal import Mammal
from ..food import Meat, Fruit, Vegetable


class Mouse(Mammal):

    def __init__(self, name, weight, living_region):
        Mammal.__init__(self, name, weight, living_region)

    @staticmethod
    def make_sound():
        return 'Squeak'

    def feed(self, food):
        if not isinstance(food, Fruit) and (not isinstance(food, Vegetable)):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.10 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Dog(Mammal):
    @staticmethod
    def make_sound():
        return 'Woof!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.40 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Cat(Mammal):
    @staticmethod
    def make_sound():
        return 'Meow'

    def feed(self, food):
        if (not isinstance(food, Meat)) and (not isinstance(food, Vegetable)):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.30 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Tiger(Mammal):
    @staticmethod
    def make_sound():
        return 'ROAR!!!'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 1.00 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"
