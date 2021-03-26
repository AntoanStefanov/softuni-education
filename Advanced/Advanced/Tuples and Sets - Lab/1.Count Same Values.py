numbers = input().split()

occurrences = {}

for num in numbers:
    num = float(num)
    if num not in occurrences:

        occurrences[num] = 0

    occurrences[num] += 1

for num, occur in occurrences.items():
    print(f"{num} - {occur} times")
