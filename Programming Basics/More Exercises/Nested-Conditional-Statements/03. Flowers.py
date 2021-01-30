number_of_chrysanthemums = int(input())
number_of_roses = int(input())
number_of_tulips = int(input())
season = input()
is_holiday = input()

if season == "Spring" or season == "Summer":
    price = number_of_chrysanthemums * 2 + \
        number_of_roses * 4.10 + number_of_tulips * 2.50
else:
    price = number_of_chrysanthemums * 3.75 + \
        number_of_roses * 4.50 + number_of_tulips * 4.15


if is_holiday == "Y":
    price += price * 0.15


if number_of_tulips >= 7 and season == "Spring":
    price = price * 0.95
elif number_of_roses >= 10 and season == "Winter":
    price = price * 0.90

if number_of_chrysanthemums + number_of_roses + number_of_tulips >= 20:
    price = price * 0.80

print(f"{price + 2:.2f}")
