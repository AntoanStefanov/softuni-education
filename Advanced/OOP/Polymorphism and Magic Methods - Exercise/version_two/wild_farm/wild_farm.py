from abc import ABC, abstractmethod


class Food(ABC):  # tozi ne e  # KLASA DA BYDE ABSTRAKTEN TRQBVA PONE 1 ABSTRAKTEN METOD !!!
    def __init__(self, quantity):
        self.quantity = quantity


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @property
    @abstractmethod
    def INCREASE_WEIGHT_PER_PIECE(self):
        pass

    @property
    @abstractmethod
    def ONLY_FOOD_EATING(self):
        pass

    def feed(self, food):

        if self.ONLY_FOOD_EATING and (not isinstance(food, self.ONLY_FOOD_EATING)):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.weight += food.quantity * self.INCREASE_WEIGHT_PER_PIECE
        self.food_eaten += food.quantity


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Vegetable(Food):
    pass


class Fruit(Food):
    pass


class Meat(Food):
    pass


class Seed(Food):
    pass


class Owl(Bird):
    INCREASE_WEIGHT_PER_PIECE = 0.25
    ONLY_FOOD_EATING = (Meat,)

    @staticmethod
    def make_sound(): return 'Hoot Hoot'


class Hen(Bird):
    INCREASE_WEIGHT_PER_PIECE = 0.35
    ONLY_FOOD_EATING = None  # (Meat, Vegetable, Seed, Fruit)

    @staticmethod
    def make_sound(): return 'Cluck'


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


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)


hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
