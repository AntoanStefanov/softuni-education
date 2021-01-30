from math import floor
from math import ceil
days_missing = int(input())
food_kg = int(input())

dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_grams = float(input())

turtle_food_per_day_kg = turtle_food_per_day_grams / 1000


total_food_per_day_kg = dog_food_per_day_kg + \
    cat_food_per_day_kg + turtle_food_per_day_kg

total_food_kg = days_missing * total_food_per_day_kg


if food_kg >= total_food_kg:
    left_food_kg = food_kg - total_food_kg
    print(f"{floor(left_food_kg)} kilos of food left.")
else:
    needed_food_kg = total_food_kg - food_kg
    print(f"{ceil(needed_food_kg)} more kilos of food are needed.")
