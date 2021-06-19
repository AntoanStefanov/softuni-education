from itertools import permutations


def possible_permutations(numbers: list):
    all_perms = permutations(numbers)
    for perm in all_perms:
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
