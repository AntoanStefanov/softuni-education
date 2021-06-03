numbers = [int(x) for x in input().split()]

even_nums = filter(lambda x: x % 2 == 0, numbers)

print(list(even_nums))

# Second time through

ints = [int(x) for x in input().split()]
print(list(filter(lambda x: x % 2 == 0, ints)))