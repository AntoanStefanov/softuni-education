# For SLavi'solve
from math import ceil
#

list_of_numbers = [int(n) for n in input().split(", ")]

max_value = 0

while len(list_of_numbers) > 0:

    max_value += 10
    group = []

    group = [num for num in list_of_numbers if num <= max_value]
    # Same as:

    # for num in list_of_numbers:
    #     if num <= max_value:
    #         group.append(num)

    list_of_numbers = [n for n in list_of_numbers if n not in group]
    # Same as:

    # for n in group:
    #     list_of_numbers.remove(n)

    print(f"Group of {max_value}'s: {group}")


# Slavi'solve


numbers = list(map(int, input().split(", ")))

max_value = max(numbers)

number_of_group = ceil(max_value / 10)


for group in range(1, number_of_group + 1):
    current_group = []

    upper_boundary = group * 10
    lower_boundary = upper_boundary - 10

    for num in numbers:
        if lower_boundary < num <= upper_boundary:
            current_group.append(num)

    print(f"Group of {group * 10}'s: {current_group}")

# With comprehension

numbers = list(map(int, input().split(", ")))

max_value = max(numbers)

number_of_group = ceil(max_value / 10)


for group in range(1, number_of_group + 1):
    upper_boundary = group * 10
    lower_boundary = upper_boundary - 10
    current_group = [
        num for num in numbers if lower_boundary < num <= upper_boundary]
    print(f"Group of {group * 10}'s: {current_group}")
