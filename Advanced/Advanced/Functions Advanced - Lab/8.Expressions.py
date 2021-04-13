from itertools import permutations, chain


data = input().split(', ')
n = len(data)  # n permutaions
perms = set(permutations(['-'] * n + ['+'] * n, n))

for p in list(perms):
    expression = ''.join(chain(*zip(p, data)))
    res = eval(expression)
    print(f'{expression}={res}')
