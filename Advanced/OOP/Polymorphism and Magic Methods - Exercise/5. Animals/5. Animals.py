from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @staticmethod
    @abstractmethod
    def make_sound(): pass

    @abstractmethod
    def __repr__(self): pass


class Dog(Animal):

    @staticmethod
    def make_sound(): return 'Woof!'

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"


class Cat(Animal):

    @staticmethod
    def make_sound(): return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"


class Kitten(Cat):

    def __init__(self, name, age, gender=None):
        super().__init__(name, age, gender)
        self.gender = 'Female'


    @staticmethod
    def make_sound(): return 'Meow'

class Tomcat(Cat):

    def __init__(self, name, age, gender=None):
        super().__init__(name, age, gender)
        self.gender = 'Male'


    @staticmethod
    def make_sound(): return 'Hiss'


d = Dog('Tony', 1, 'Male')
print(d)
