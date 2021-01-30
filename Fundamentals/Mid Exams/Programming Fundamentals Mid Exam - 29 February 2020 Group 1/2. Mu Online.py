health = 100
bitcoins = 0


rooms = input().split("|")

best_room = 0
completed_quest = True

for room in rooms:

    command, number = room.split(" ")
    number = int(number)

    if command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
        best_room += 1
    elif command == "potion":
        
        if health + number >= 100:
            healed = 100 - health
            health = 100

        else:
            health = health + number
            healed = number

        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")

        best_room += 1

    else:
        best_room += 1
        if health - number > 0:
            health -= number
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            completed_quest = False
            break

if completed_quest:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
