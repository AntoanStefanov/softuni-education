class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        if room not in self.rooms:
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            current_room_expense = room.expenses + room.room_cost
            total += current_room_expense
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        res = []
        for room in self.rooms:
            current_room_expense = room.expenses + room.room_cost
            if room.budget >= current_room_expense:
                room.budget -= current_room_expense
                res.append(f"{room.family_name} paid {current_room_expense:.2f}$ and have {room.budget:.2f}$ left.")
            else:
                res.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return '\n'.join(res)

    def status(self):
        info = ''
        members = 0
        for room in self.rooms:
            members += room.members_count
            info += f'Total population: {members}\n'
            info += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                index = 1
                for child in room.children:
                    info += f'--- Child {index} monthly cost: {child.get_monthly_expense():.2f}$\n'
                    index += 1
            if room.appliances:
                cost = 0
                for app in room.appliances:
                    cost += app.get_monthly_expense()
                info += f'--- Appliances monthly cost: {cost:.2f}\n'

        return info[:-1]
