clients = int(input())

total_spend_money = 0

for i in range(1, clients + 1):
    purchase = input()
    spend_money = 0
    items = 0
    while purchase != "Finish":

        if purchase == "basket":
            spend_money += 1.50
        elif purchase == "wreath":
            spend_money += 3.80
        elif purchase == "chocolate bunny":
            spend_money += 7
        items += 1

        purchase = input()

    if items % 2 == 0:
        spend_money -= spend_money * 0.20
    print(f"You purchased {items} items for {spend_money:.2f} leva.")

    total_spend_money += spend_money

print(f"Average bill per client is: {total_spend_money / clients:.2f} leva.")
