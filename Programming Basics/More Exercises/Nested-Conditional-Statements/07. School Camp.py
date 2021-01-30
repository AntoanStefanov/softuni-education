season = input()

group_type = input()

number_of_students = int(input())

number_of_nights = int(input())


if group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"


if group_type == "mixed":
    if season == "Winter":
        price_for_night = 10
    elif season == "Spring":
        price_for_night = 9.50
    elif season == "Summer":
        price_for_night = 20
else:
    if season == "Winter":
        price_for_night = 9.60
    elif season == "Spring":
        price_for_night = 7.20
    elif season == "Summer":
        price_for_night = 15

price = number_of_students * number_of_nights * price_for_night

if number_of_students >= 50:
    price -= price * 0.50
elif 20 <= number_of_students < 50:
    price -= price * 0.15
elif 10 <= number_of_students < 20:
    price -= price * 0.05

print(f"{sport}{price: .2f} lv.")
