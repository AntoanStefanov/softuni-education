season = input()

km_for_month = float(input())

total_km = km_for_month * 4

if km_for_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75
    elif season == "Summer":
        price_per_km = 0.90
    elif season == "Winter":
        price_per_km = 1.05
elif 5000 < km_for_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95
    elif season == "Summer":
        price_per_km = 1.10
    elif season == "Winter":
        price_per_km = 1.25
else:
    price_per_km = 1.45


total_price = total_km * price_per_km * 90/100

# taxes = (total_km * price_per_km) * 0.10

# price = total_price - taxes


print(f"{total_price:.2f}")
