budget = float(input())
number_of_nights = int(input())
night_price = float(input())
percent_of_extra_expenses = int(input())

if number_of_nights > 7:
    night_price *= 0.95

total_nights_price = number_of_nights * night_price

extra_expenses = (budget * percent_of_extra_expenses) / 100

total_price = total_nights_price + extra_expenses

if budget >= total_price:
    print(
        f"Ivanovi will be left with {budget - total_price:.2f} leva after vacation.")
else:
    print(f"{total_price - budget:.2f} leva needed.")
