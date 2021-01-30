fires = input().split("#")
water = int(input())
effort = 0
total_fire_out = 0
cells = []
for fire in fires:

    type_of_fire, range_of_fire = fire.split(" = ")

    range_of_fire = int(range_of_fire)

    if (type_of_fire == "High") and (81 <= range_of_fire <= 125) and (water >= range_of_fire):

        cells.append(range_of_fire)
        water -= range_of_fire
        effort += range_of_fire * 0.25
        total_fire_out += range_of_fire

    elif (type_of_fire == "Medium") and (51 <= range_of_fire <= 80) and (water >= range_of_fire):

        cells.append(range_of_fire)
        water -= range_of_fire
        effort += range_of_fire * 0.25
        total_fire_out += range_of_fire

    elif (type_of_fire == "Low") and (1 <= range_of_fire <= 50) and (water >= range_of_fire):

        cells.append(range_of_fire)
        water -= range_of_fire
        effort += range_of_fire * 0.25
        total_fire_out += range_of_fire

print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire_out}")


########## SECOND TIME SOLVING #################


data = input().split('#')
water = int(input())

total_effort = 0
total_fire = 0

print('Cells:')
for fire in data:

    fire_level, value = fire.split(' = ')
    value = int(value)
    is_valid = True

    if fire_level == 'High' and 81 <= value <= 125:
        pass

    elif fire_level == 'Medium' and 51 <= value <= 80:
        pass

    elif fire_level == 'Low' and 1 <= value <= 50:
        pass

    else:
        is_valid = False

    if is_valid:

        if value > water:
            continue

        print(f' - {value}')
        water -= value
        effort = value * 0.25
        total_effort += effort
        total_fire += value

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')
