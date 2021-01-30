budget = float(input())
number_of_extras = int(input())
extra_outfit_price = float(input())

decor = budget * 0.10

if number_of_extras > 150:
    extra_outfit_price *= 0.90

total_expenses = decor + (number_of_extras * extra_outfit_price)

if total_expenses <= budget:
    print(
        f"Action!\nWingard starts filming with {budget-total_expenses:.2f} leva left.")
else:
    print(
        f"Not enough money!\nWingard needs {total_expenses - budget:.2f} leva more.")
