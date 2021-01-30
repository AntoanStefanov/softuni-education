product = input()
day = input()
quantity = float(input())
price = 0
if day == "Saturday" or day == "Sunday":
    if product == "banana":
        price += 2.70 * quantity
    elif product == "apple":
        price += 1.25 * quantity
    elif product == "orange":
        price += 0.90 * quantity
    elif product == "grapefruit":
        price += 1.60 * quantity
    elif product == "kiwi":
        price += 3.00 * quantity
    elif product == "pineapple":
        price += 5.60 * quantity
    elif product == "grapes":
        price += 4.20 * quantity
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if product == "banana":
        price += 2.50 * quantity
    elif product == "apple":
        price += 1.20 * quantity
    elif product == "orange":
        price += 0.85 * quantity
    elif product == "grapefruit":
        price += 1.45 * quantity
    elif product == "kiwi":
        price += 2.70 * quantity
    elif product == "pineapple":
        price += 5.50 * quantity
    elif product == "grapes":
        price += 3.85 * quantity
if price != 0:
    print(f"{price:.2f}")
else:
    print("error")
