class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting
    
    @property
    def name(self):
        return self.__name
    
    def __str__(self):
        res = ''
        res += f"Player: {self.name}\n"
        res += f"Sprint: {self.__sprint}\n"
        res += f"Dribble: {self.__dribble}\n"
        res += f"Passing: {self.__passing}\n"
        res += f"Shooting: {self.__shooting}\n"
        return res