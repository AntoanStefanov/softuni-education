stadium_capacity = int(input())
number_of_fans = int(input())

sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0

for fan in range(1, number_of_fans + 1):
    fan_sector = input()

    if fan_sector == "A":
        sector_A += 1
    elif fan_sector == "B":
        sector_B += 1
    elif fan_sector == "V":
        sector_V += 1
    elif fan_sector == "G":
        sector_G += 1


print(f"{sector_A / number_of_fans * 100:.2f}%")
print(f"{sector_B / number_of_fans * 100:.2f}%")
print(f"{sector_V / number_of_fans * 100:.2f}%")
print(f"{sector_G / number_of_fans * 100:.2f}%")
print(f"{number_of_fans / stadium_capacity * 100:.2f}%")
