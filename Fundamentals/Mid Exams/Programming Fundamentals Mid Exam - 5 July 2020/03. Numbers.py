numbers = [int(num) for num in input().split()]
numbers = sorted(numbers, reverse=True)
average_value = sum(numbers) / len(numbers)


top_five = []
are_five = False
for num in numbers:
    if num > average_value:
        top_five.append(num)
        if len(top_five) == 5:
            are_five = True
            break

if not top_five:
    print("No")
for num in top_five:
    print(num, end=' ')
