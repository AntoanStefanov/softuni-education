from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Fruit(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Meat(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Seed(Food):
    def __init__(self, quantity):
        super().__init__(quantity)


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass


class Bird(Animal):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size


class Mammal(Animal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region


class Owl(Bird):

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{type(self).__name__} does not eat {type(food).__name__}!"
        self.food_eaten += food.quantity
        self.weight += 0.25 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Hen(Bird):

    @staticmethod
    def make_sound():
        return 'Cluck'

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += 0.35 * food.quantity

    def __repr__(self):
        return f"{type(self).__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


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
