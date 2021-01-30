from math import ceil
number_of_people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entrance_fee = entrance_fee * number_of_people
number_of_sunbeds = ceil(number_of_people * 0.75)
total_sunbed_price = number_of_sunbeds * sunbed_price
number_of_umbrellas = ceil(number_of_people * 0.50)
total_umbrella_price = number_of_umbrellas * umbrella_price

total_price = total_entrance_fee + total_sunbed_price + total_umbrella_price
print(f"{total_price:.2f} lv.")
