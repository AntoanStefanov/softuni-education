class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                message = room.take_room(people)
                if message:
                    return message
                self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                guests_to_remove = room.guests
                messsage = room.free_room()
                if messsage:
                    return messsage
                self.guests -= guests_to_remove

    def status(self):
        stat = f"Hotel {self.name} has {self.guests} total guests\n"
        taken_rooms_numbers = []
        free_rooms_numbers = []
        for room in self.rooms:
            if room.is_taken:
                taken_rooms_numbers.append(str(room.number))
            else:
                free_rooms_numbers.append(str(room.number))
        stat += f'Free rooms: {", ".join(free_rooms_numbers)}\n'
        stat += f'Taken rooms: {", ".join(taken_rooms_numbers)}'
        return stat


########## NOT USING SELF.GUESTS(HOTEL GUESTS)#####
############ EASIER IMPLEMENTATION - using for loop rooms and thier guests ############


# class Hotel:
#     def __init__(self, name):
#         self.name = name
#         self.rooms = []
#         self.guests = 0

#     @classmethod
#     def from_stars(cls, stars_count):
#         return cls(f'{stars_count} stars Hotel')

#     def add_room(self, room):
#         self.rooms.append(room)

#     def take_room(self, room_number, people):
#         for room in self.rooms:
#             if room.number == room_number:
#                 room.take_room(people)

#     def free_room(self, room_number):
#         for room in self.rooms:
#             if room.number == room_number:
#                 room.free_room()

#     def status(self):
#         total_guests = 0
#         for room in self.rooms:
#             total_guests += room.guests
#         stat = f"Hotel {self.name} has {total_guests} total guests\n"
#         taken_rooms_numbers = []
#         free_rooms_numbers = []
#         for room in self.rooms:
#             if room.is_taken:
#                 taken_rooms_numbers.append(str(room.number))
#             else:
#                 free_rooms_numbers.append(str(room.number))
#         stat += f'Free rooms: {", ".join(free_rooms_numbers)}\n'
#         stat += f'Taken rooms: {", ".join(taken_rooms_numbers)}'
#         return stat
