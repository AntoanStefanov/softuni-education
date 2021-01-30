
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
