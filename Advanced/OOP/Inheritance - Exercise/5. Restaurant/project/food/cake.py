from .dessert import Dessert


class Cake(Dessert):
    PRICE = 5
    GRAMS = 250
    CALORIES = 1000

    def __init__(self, name):
        super().__init__(name, self.PRICE, Cake.GRAMS, self.CALORIES)
