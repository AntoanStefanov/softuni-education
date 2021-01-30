voucher_value = int(input())

tickets = 0
other_things = 0

purchase = input()
while purchase != "End":
    if len(purchase) > 8:
        price = ord(purchase[0]) + ord(purchase[1])
        if voucher_value < price:
            break
        tickets += 1
    else:
        price = ord(purchase[0])
        if voucher_value < price:
            break
        other_things += 1
    voucher_value -= price

    purchase = input()
print(f"{tickets}\n{other_things}")
