flower = input()
number_of_flowers = int(input())
budget = int(input())

price_for_1_rose = 5
price_for_1_dahlia = 3.80
price_for_1_tulip = 2.80
price_for_1_narcissus = 3
price_for_1_gladiolus = 2.50

price = 0

if flower == "Roses":
    price += price_for_1_rose * number_of_flowers
    if number_of_flowers > 80:
        price -= price * 0.10
elif flower == "Dahlias":
    price += price_for_1_dahlia * number_of_flowers
    if number_of_flowers > 90:
        price -= price * 0.15
elif flower == "Tulips":
    price += price_for_1_tulip * number_of_flowers
    if number_of_flowers > 80:
        price -= 0.15 * price
elif flower == "Narcissus":
    price += price_for_1_narcissus * number_of_flowers
    if number_of_flowers < 120:
        price += 0.15 * price
elif flower == "Gladiolus":
    price += price_for_1_gladiolus * number_of_flowers
    if number_of_flowers < 80:
        price += 0.20 * price

if price > budget:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
else:
    left_money = budget - price
    print(
        f"Hey, you have a great garden with {number_of_flowers} {flower} and {left_money:.2f} leva left.")
