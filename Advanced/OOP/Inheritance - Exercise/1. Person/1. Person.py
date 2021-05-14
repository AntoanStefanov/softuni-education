class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Child(Person):
    # ЗАЩО Е  НУЖЕН __init__ метод в Child class, като работи и така ? Минава през
    # inita на Person class
    # def __init__(self, name, age):
    #     super().__init__(name, age)
    # И само с pass работи
    pass


person = Person("Peter", 25)
child = Child("Peter Junior", 5)
print(person.name)
print(person.age)
print(child.__class__.__bases__[0].__name__)
