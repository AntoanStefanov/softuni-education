max_capacity = 255
quantity_of_water_poured = 0

number_of_inputs = int(input())
for inpt in range(1, number_of_inputs + 1):
    water = int(input())
    quantity_of_water_poured += water
    if quantity_of_water_poured > max_capacity:
        quantity_of_water_poured -= water
        print("Insufficient capacity!")
print(quantity_of_water_poured)
