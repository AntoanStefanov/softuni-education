from itertools import combinations, permutations
help(combinations)
help(permutations)
string = input()

perms = permutations(string, len(string))

for p in perms:
    print(''.join(p))
