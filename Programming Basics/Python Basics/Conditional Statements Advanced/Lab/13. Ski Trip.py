days = int(input())
room = input()
rate = input()

nights = days - 1
discount = 0


if room == "room for one person":
    price = nights * 18
elif room == "apartment":
    price = nights * 25
    if nights < 10:
        discount = 0.30
    elif 10 <= nights <= 15:
        discount = 0.35
    elif nights > 15:
        discount = 0.50
elif room == "president apartment":
    price = nights * 35
    if nights < 10:
        discount = 0.10
    elif 10 <= nights <= 15:
        discount = 0.15
    elif nights > 15:
        discount = 0.20

total_price = price - price * discount


if rate == "positive":
    total_price += total_price * 0.25
else:
    total_price -= total_price * 0.10

print(f"{total_price:.2f}")
