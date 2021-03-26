from collections import defaultdict


numbers = input().split()
# If the key doesn't exist in the dict, factory will construct the key and value 0'
occurrences = defaultdict(int)  # default factory  int , which will return 0 !

for num in numbers:
    num = float(num)
    occurrences[num] += 1

for num, occur in occurrences.items():
    print(f"{num} - {occur} times")


# Second solution

numbers = input().split()

occurrences = {}

for num in numbers:
    num = float(num)
    if num not in occurrences:

        occurrences[num] = 0

    occurrences[num] += 1

for num, occur in occurrences.items():
    print(f"{num} - {occur} times")
