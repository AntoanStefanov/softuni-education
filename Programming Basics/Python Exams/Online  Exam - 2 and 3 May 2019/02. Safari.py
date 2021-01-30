budget = float(input())
fuel_needed = float(input())
day_of_week = input()

fuel_price = fuel_needed * 2.10

total_price = fuel_price + 100  # tour-guide

if day_of_week == "Saturday":
    total_price *= 0.90
if day_of_week == "Sunday":
    total_price *= 0.80
difference = abs(budget - total_price)
if total_price > budget:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")
else:
    print(f"Safari time! Money left: {difference:.2f} lv.")
