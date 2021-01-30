bought_food_in_kg = int(input())
command = input()
bought_food_in_grams = bought_food_in_kg * 1000
total_eaten_food_in_grams = 0

while command != "Adopted":
    eaten_food_in_grams_for_one_time = int(command)
    total_eaten_food_in_grams += eaten_food_in_grams_for_one_time
    command = input()


if total_eaten_food_in_grams <= bought_food_in_grams:
    print(
        f"Food is enough! Leftovers: {bought_food_in_grams - total_eaten_food_in_grams} grams.")
else:
    print(
        f"Food is not enough. You need {total_eaten_food_in_grams - bought_food_in_grams} grams more.")
