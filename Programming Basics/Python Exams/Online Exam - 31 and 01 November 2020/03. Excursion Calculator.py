people = int(input())
season = input()

if season == "spring":
    if people <= 5:
        price_for_one_person = 50
    else:
        price_for_one_person = 48
elif season == "summer":
    if people <= 5:
        price_for_one_person = 48.50
    else:
        price_for_one_person = 45
elif season == "autumn":
    if people <= 5:
        price_for_one_person = 60
    else:
        price_for_one_person = 49.50
elif season == "winter":
    if people <= 5:
        price_for_one_person = 86
    else:
        price_for_one_person = 85

price_for_all = people * price_for_one_person

if season == "summer":
    price_for_all = price_for_all - (price_for_all * 0.15)
elif season == "winter":
    price_for_all = price_for_all + (price_for_all * 0.08)

print(f"{price_for_all:.2f} leva.")
