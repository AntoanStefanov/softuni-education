working_day_events = input().split("|")

energy = 100
coins = 100

for working_day in working_day_events:

    event, number = working_day.split("-")

    if event == "rest":
        if (energy + int(number)) > 100:
            gained = 100 - energy
            energy = 100
        else:
            energy += int(number)
            gained = int(number)

        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue

        coins += int(number)
        energy -= 30
        print(f"You earned {number} coins.")

    else:
        ingredient = event
        coins -= int(number)

        if coins > 0:
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


###### second Solution ####


coins = 100
energy = 100

events = input().split('|')


for event in events:

    event, value = event.split('-')

    value = int(value)

    if event == 'rest':
        if value + energy >= 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            print(f"You gained {value} energy.")
            energy += value
        print(f"Current energy: {energy}.")
    elif event == 'order':
        if energy - 30 < 0:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
    else:
        ingredient = event
        coins -= value
        if coins <= 0:
            print(f"Closed! Cannot afford {ingredient}.")
            break
        else:
            print(f"You bought {ingredient}.")
else:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
