# Защо при наследяване викаме init и защо в него викаме super().init 
# и то без self ? Ако имат едни и същи аргументи 


class Hero:

    def __init__(self, username, level):
        self.username = username
        self.level = level

    def __repr__(self):
        return f"{self.username} of type {type(self).__name__} has level {self.level}"


class Elf(Hero):

    def __init__(self, username, level):
        super().__init__(username, level)


class MuseElf(Elf):

    def __init__(self, username, level):
        super().__init__(username, level)


class Wizard(Hero):

    def __init__(self, username, level):
        super().__init__(username, level)


class DarkWizard(Wizard):

    def __init__(self, username, level):
        super().__init__(username, level)


class SoulMaster(DarkWizard):

    def __init__(self, username, level):
        super().__init__(username, level)


class Knight(Hero):

    def __init__(self, username, level):
        super().__init__(username, level)


class DarkKnight(Knight):

    def __init__(self, username, level):
        super().__init__(username, level)


class BladeKnight(DarkKnight):

    def __init__(self, username, level):
        super().__init__(username, level)


hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)
