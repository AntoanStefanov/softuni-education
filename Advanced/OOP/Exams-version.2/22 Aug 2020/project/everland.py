from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        info = ''
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                room.budget -= room.expenses + room.room_cost
                info += f"{room.family_name} paid {room.expenses + room.room_cost:.2f}$ and have {room.budget:.2f}$ left.\n"
            else:
                info += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return info[:-1]

    def status(self):
        status = f'Total population: {sum([room.members_count for room in self.rooms])}\n'
        for room in self.rooms:
            status += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                for number, child in enumerate(room.children):
                    status += f'--- Child {number + 1} monthly cost: {child.get_monthly_expense():.2f}$\n'
            status += f'--- Appliances monthly cost: {sum([app.get_monthly_expense() for app in room.appliances]):.2f}$\n'
        return status[:-1]
