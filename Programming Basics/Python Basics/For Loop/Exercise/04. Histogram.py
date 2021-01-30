n = int(input())

first_range = 0
second_range = 0
third_range = 0
forth_range = 0
fifth_range = 0


for number in range(1, n + 1):
    element = int(input())

    if element < 200:
        first_range += 1
    elif element < 400:
        second_range += 1
    elif element < 600:
        third_range += 1
    elif element < 800:
        forth_range += 1
    elif element >= 800:
        fifth_range += 1


first_range_percent = first_range / n * 100
second_range_percent = second_range / n * 100
third_range_percent = third_range / n * 100
forth_range_percent = forth_range / n * 100
fifth_range_percent = fifth_range / n * 100

print(f"{first_range_percent:.2f}%")
print(f"{second_range_percent:.2f}%")
print(f"{third_range_percent:.2f}%")
print(f"{forth_range_percent:.2f}%")
print(f"{fifth_range_percent:.2f}%")
