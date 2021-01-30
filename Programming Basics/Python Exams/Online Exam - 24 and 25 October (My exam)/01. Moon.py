from math import ceil
average_speed = float(input())
needed_fuel_for_100_km = float(input())

total_distance = 384400 * 2

total_time = ceil(total_distance / average_speed) + 3
print(total_time)
fuel = int((needed_fuel_for_100_km * total_distance) / 100)
print(fuel)
