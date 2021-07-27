from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    room_cost = 10
    appliances = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        # Calculate the expenses of each appliance
        self.calculate_expenses(self.appliances)

    # self.calculate_expenses(self.appliances)  # Защо не мога да изчисля тук ?
