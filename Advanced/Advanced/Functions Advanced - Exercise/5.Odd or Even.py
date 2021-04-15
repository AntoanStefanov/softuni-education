command = input()

numbers = [int(x) for x in input().split()]

if command == 'Odd':
    odd_nums = list(filter(lambda x: x % 2 == 1, numbers))
    print(sum(odd_nums) * len(numbers))
elif command == 'Even':
    even_nums = list(filter(lambda x: x % 2 == 0, numbers))
    print(sum(even_nums) * len(numbers))
