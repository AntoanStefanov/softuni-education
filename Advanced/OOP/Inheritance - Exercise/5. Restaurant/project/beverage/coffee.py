from .hot_beverage import HotBeverage


class Coffee(HotBeverage):
    MILLILITERS = 50  # (constant)
    PRICE = 3.50  # (constant)
    # caffeine - float

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self): return self.__caffeine
