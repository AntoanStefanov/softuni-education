class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars):
        name = f'{stars} stars Hotel'
        return cls(name)

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                return room.free_room()

    def print_status(self):
        taken = []
        free = []
        for room in self.rooms:
            if room.is_taken:
                taken.append(room.number)
                self.guests += room.guests
            else:
                free.append(room.number)

        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join([str(n) for n in free])}")
        print(f"Taken rooms: {', '.join([str(n) for n in taken])}")
