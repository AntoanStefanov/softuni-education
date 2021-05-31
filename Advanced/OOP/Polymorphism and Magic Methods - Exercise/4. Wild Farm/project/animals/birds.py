from .animal import Bird
from ..food import Meat


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


b = Owl('tony', 1, 2)
print(b)
