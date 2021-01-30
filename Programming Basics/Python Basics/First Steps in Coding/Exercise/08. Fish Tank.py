length = int(input())
width = int(input())
height = int(input())
percentage_occupied_by_volume = float(input())
tank_volume = length * width * height
total_liters_that_will_collect = tank_volume * 0.001
percent = percentage_occupied_by_volume * 0.01
liters_needed = total_liters_that_will_collect * (1 - percent)
print(liters_needed)
