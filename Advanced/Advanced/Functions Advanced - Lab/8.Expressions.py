from itertools import permutations


data = [int(n) for n in input().split(', ')]


perms = permutations(data)

for p in list(perms):
    print(p)
 