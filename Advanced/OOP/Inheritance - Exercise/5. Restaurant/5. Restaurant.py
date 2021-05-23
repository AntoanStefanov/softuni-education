# Защо тук https://prnt.sc/12vhhy3 - обектът person има name, age  и
# _Person__name и _Person__age ?
# Не трябва ли да има само private атрибутите (_Person__name и _Person__age) ?
# След като self.age и self.name викат setter-и ?


# МОГАТ ЛИ CLASS VARIABLES ДА ИМАТ ГЕТЕРИ И СЕТЕРИ
# @property
# def milliliters: return Coffee.__milliliters

# @classproperty

class Product:

    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    @property
    def name(self): return self.__name

    @property
    def price(self): return self.__price


class Beverage(Product):

    def __init__(self, name, price, milliliters):
        super().__init__(name, price)
        self.__milliliters = milliliters

    @property
    def milliliters(self): return self.__milliliters


class Food(Product):

    def __init__(self, name, price, grams):
        super().__init__(name, price)
        self.__grams = grams

    @property
    def grams(self): return self.__grams


class HotBeverage(Beverage):
    pass


class ColdBeverage(Beverage):
    pass


class Coffee(HotBeverage):
    MILLILITERS = 50  # (constant)
    PRICE = 3.50  # (constant)
    # caffeine - float

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.PRICE, self.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self): return self.__caffeine


class Tea(HotBeverage):
    pass


class MainDish(Food):
    pass


class Dessert(Food):
    def __init__(self, name, price, grams, calories):
        super().__init__(name, price, grams)
        self.__calories = calories

    @property
    def calories(self): return self.__calories


class Starter(Food):
    pass


class Salmon(MainDish):
    GRAMS = 22  # __GRAMS = 22

    def __init__(self, name, price):
        super().__init__(name, price, self.GRAMS) # Salmon.GRAMS


class Soup(Starter):
    pass


class Cake(Dessert):
    PRICE = 5
    GRAMS = 250
    CALORIES = 1000

    def __init__(self, name):
        super().__init__(name, self.PRICE, Cake.GRAMS, self.CALORIES)


product = Product("coffee", 2.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
beverage = Beverage("coffee", 2.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
