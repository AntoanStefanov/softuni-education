people = int(input())
days = int(input())

coins = days * 50

for day in range(1, days + 1):

    if day % 10 == 0:
        people -= 2

    if day % 15 == 0:
        people += 5

    coins -= (people * 2)

    if day % 3 == 0:
        coins -= (people * 3)

    if day % 5 == 0:
        coins += (people * 20)
        if day % 3 == 0:
            coins -= (people * 2)

print(f"{people} companions received {coins // people} coins each.")
