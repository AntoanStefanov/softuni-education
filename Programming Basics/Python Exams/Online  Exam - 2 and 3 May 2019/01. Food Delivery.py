number_of_chicken_menu = int(input())
number_of_fish_menu = int(input())
number_of_vegetarian_menu = int(input())


price = (number_of_chicken_menu * 10.35) + \
    (number_of_fish_menu * 12.40) + (number_of_vegetarian_menu * 8.15)

dessert = price * 0.20

total_price = price + dessert + 2.50
print(f"Total: {total_price:.2f}")
