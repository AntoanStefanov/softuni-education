from sys import maxsize

numbers = int(input())

total_sum = 0
max_element = -maxsize

for number in range(1, numbers + 1):
    element = int(input())

    total_sum += element

    if element > max_element:
        max_element = element


remaining_sum = total_sum - max_element

if remaining_sum == max_element:
    print(f"Yes\nSum = {max_element}")
else:
    print(f"No\nDiff = {abs(remaining_sum-max_element)}")
