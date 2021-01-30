from math import ceil

number_of_guests = int(input())
budget = float(input())


needed_breads = ceil(number_of_guests / 3)  # нужни козунаци
needed_eggs = number_of_guests * 2  # нужни яйца


breads_price = needed_breads * 4
eggs_price = needed_eggs * 0.45

total_price = breads_price + eggs_price

if budget >= total_price:
    print(
        f"Lyubo bought {needed_breads} Easter bread and {needed_eggs} eggs.")
    print(f"He has {budget - total_price:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {total_price - budget:.2f} lv. more.")
