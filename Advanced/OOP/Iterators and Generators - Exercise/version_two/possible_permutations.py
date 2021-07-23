import itertools


def possible_permutations(integers):
    for perm in itertools.permutations(integers):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]
