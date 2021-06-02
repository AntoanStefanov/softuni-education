from .cat import Cat
class Kitten(Cat):

    def __init__(self, name, age, gender=None):
        super().__init__(name, age, gender)
        self.gender = 'Female'


    @staticmethod
    def make_sound(): return 'Meow'