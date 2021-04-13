from itertools import permutations, chain, product


data = input().split(', ')
n = len(data)  # n permutaions
perms = set(permutations(['-'] * n + ['+'] * n, n))

for p in list(perms):
    expression = ''.join(chain(*zip(p, data)))
    res = eval(expression)
    print(f'{expression}={res}')

####################


numbers = input().split(', ')
n = len(numbers)

cartesian_product = [list(x) for x in (product('+-', repeat=n))]

for signs in cartesian_product:
    elements = [''.join(x) for x in list(zip(signs, numbers))]
    expression = ''.join(elements)
    print(f'{expression}={eval(expression)}')
