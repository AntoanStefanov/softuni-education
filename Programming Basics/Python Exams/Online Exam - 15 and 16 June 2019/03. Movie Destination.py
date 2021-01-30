budget = float(input())
destination = input()
season = input()
number_of_days = int(input())


if destination == "Dubai":
    if season == "Summer":
        price = 40_000
    elif season == "Winter":
        price = 45_000
elif destination == "Sofia":
    if season == "Summer":
        price = 12_500
    elif season == "Winter":
        price = 17_000
elif destination == "London":
    if season == "Summer":
        price = 20_250
    elif season == "Winter":
        price = 24_000


total_price = number_of_days * price

if destination == "Dubai":
    total_price *= 0.70
elif destination == "Sofia":
    total_price *= 1.25

if budget >= total_price:
    print(
        f"The budget for the movie is enough! We have {budget - total_price:.2f} leva left!")
else:
    print(f"The director needs {total_price - budget:.2f} leva more!")
