film_budget = float(input())
extras = int(input())
price_for_extra_clothing = float(input())

decor_price = film_budget * 0.10
clothing_price = extras * price_for_extra_clothing
if extras > 150:
    clothing_price -= clothing_price * 0.10


total_film_money = decor_price + clothing_price


if total_film_money > film_budget:
    money_needed = total_film_money - film_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = film_budget - total_film_money
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
 ################### OR #############

movie_budget = float(input())
statists = int(input())
price_outfit = float(input())

decor_price = 10/100 * movie_budget
total_price_outfit = statists * price_outfit

if statists > 150:
    total_price_outfit -= total_price_outfit * 10/100

total_movie_price = decor_price + total_price_outfit


if total_movie_price > movie_budget:
    money_needed = total_movie_price - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = movie_budget - total_movie_price
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
