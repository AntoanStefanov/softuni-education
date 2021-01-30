days = int(input())

food_quantity = float(input())

dog_eaten_food = 0
cat_eaten_food = 0
biscuits = 0


for i in range(1, days + 1):
    quantity_eaten_dog_food = int(input())
    quantity_eaten_cat_food = int(input())

    dog_eaten_food += quantity_eaten_dog_food
    cat_eaten_food += quantity_eaten_cat_food

    if i % 3 == 0:
        biscuits += (quantity_eaten_dog_food + quantity_eaten_cat_food) * 0.10


total_eaten_food = dog_eaten_food + cat_eaten_food

dog_percent = (dog_eaten_food / total_eaten_food) * 100
cat_percent = (cat_eaten_food / total_eaten_food) * 100
total_percent = (total_eaten_food / food_quantity) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")
