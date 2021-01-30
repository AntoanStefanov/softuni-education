minutes_walks_per_day = int(input())
walks = int(input())
calories_per_day = int(input())

total_minutes = minutes_walks_per_day * walks
burned_calories = total_minutes * 5


needed_burned_calories = calories_per_day * 0.50


if burned_calories >= needed_burned_calories:
    print(
        f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(
        f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
