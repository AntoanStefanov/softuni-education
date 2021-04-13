from itertools import combinations

names = input().split(', ')
chairs = int(input())

combs = list(combinations(names, chairs))

[print(*c, sep=", ") for c in combs]
