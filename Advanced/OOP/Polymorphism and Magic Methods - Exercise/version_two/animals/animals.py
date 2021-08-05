from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"


class Dog(Animal):

    @staticmethod
    def make_sound(): return 'Woof!'

class Cat(Animal):

    @staticmethod
    def make_sound(): return 'Meow meow!'

class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Female')


    @staticmethod
    def make_sound(): return 'Meow'

class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, 'Male')

    @staticmethod
    def make_sound(): return 'Hiss'