class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print(f"My name is {self.name}")


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)


class Person:
    def __init__(self, name, personality, is_sitting):  # robot_owned
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        # self.robot_owned = robot_owned

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


# НОВИЯ ОБЕКТ ИМА - ALICE като име , aggressive като personality и False за is_sitting
p1 = Person("Alice", "aggressive", False)
p2 = Person("Becky", "talkative", True)

# p1 притежава r1
# Или като добавиш параметър в контруктура "robot_owned"
# Или
p1.robot_owned = r2
# Така създаваме нов атрибут в p1 , наречен robot_owned
p2.robot_owned = r1

p1.robot_owned.introduce_self()
