from sys import maxsize
n = int(input())

max_value = -maxsize
min_value = maxsize

for number in range(1, n + 1):
    value = int(input())

    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value


print(f"Max number: {max_value}")
print(f"Min number: {min_value}")
