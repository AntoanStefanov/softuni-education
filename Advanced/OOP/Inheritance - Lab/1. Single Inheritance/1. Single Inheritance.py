class Animal:

    @staticmethod
    def eat(): return 'eating...'


animal = Animal()


class Dog(Animal):

    @staticmethod
    def bark(): return 'barking...'


dog = Dog()

print(dog.eat())
print(dog.bark())
