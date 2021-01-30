number_of_floors = int(input())
number_of_rooms = int(input())

for floors in range(number_of_floors, 0, -1):
    for rooms in range(number_of_rooms):
        if floors == number_of_floors:
            print(f"L{floors}{rooms}", end=" ")
        elif floors % 2 == 1:
            print(f"A{floors}{rooms}", end=" ")
        elif floors % 2 == 0:
            print(f"O{floors}{rooms}", end=" ")
    print()
