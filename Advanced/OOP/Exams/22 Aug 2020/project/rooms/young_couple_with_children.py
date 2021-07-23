from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    room_cost = 30

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.children = list(children)
        tvs = [TV() for person in range(2 + len(children))]
        fridges = [Fridge() for person in range(2 + len(children))]
        laptops = [Laptop() for person in range(2 + len(children))]
        self.appliances = tvs + fridges + laptops
        self.calculate_expenses(self.appliances, self.children)

    # Calculate the expenses (appliances and children expenses).


