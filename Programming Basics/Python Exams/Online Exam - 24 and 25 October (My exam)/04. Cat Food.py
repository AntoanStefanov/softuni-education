number_of_cats = int(input())
group_1 = 0
group_2 = 0
group_3 = 0
total_grams = 0
for cat in range(1, number_of_cats + 1):
    grams_of_food = float(input())

    if 100 <= grams_of_food < 200:
        group_1 += 1
    elif 200 <= grams_of_food < 300:
        group_2 += 1
    elif 300 <= grams_of_food < 400:
        group_3 += 1
    total_grams += grams_of_food


total_kg = total_grams / 1000
total_price = total_kg * 12.45
print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {round(total_price,2)} lv.")
