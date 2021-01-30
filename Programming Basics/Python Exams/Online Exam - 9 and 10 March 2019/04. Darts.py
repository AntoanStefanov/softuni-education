player_name = input()

player_points = 301
sucessful_shots = 0
unsucessful_shots = 0

area = input()

while area != "Retire":
    points = int(input())
    if area == "Triple":
        points *= 3
    elif area == "Double":
        points *= 2

    if points > player_points:
        unsucessful_shots += 1
        pass
    elif player_points >= points:
        player_points -= points
        sucessful_shots += 1
        if player_points == 0:
            print(f"{player_name} won the leg with {sucessful_shots} shots.")
            break

    area = input()
else:
    print(f"{player_name} retired after {unsucessful_shots} unsuccessful shots.")