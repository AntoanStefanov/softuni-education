numbers = [int(n) for n in input().split(', ')]

positive_numbers = [num for num in numbers if num >= 0]
negative_numbers = [num for num in numbers if num < 0]
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 == 1]


print(f'Positive: {", ".join([str(num) for num in positive_numbers])}')

print(f'Negative: {", ".join([str(num) for num in negative_numbers])}')

print(f'Even: {", ".join([str(num) for num in even_numbers])}')

print(f'Odd: {", ".join([str(num) for num in odd_numbers])}')
