


def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(4, 5, 6, 1, 3))

################
# reduce() - редуциране . 1-ви аргумент приема функция, която бива извиквана
# втори аргумент - последователност , обект, който може да е обходен
# Inital - opitnal third parameter

from functools import reduce


def multiply1(*args):
    # първия аргумент (функцията) задължително приема два аргумента
    return reduce(lambda a, b: a * b, args)


# Взима два по два аргумента в ламбдата и връща резултата в последователността до изчерпване
print(multiply(1, 2, 3, 4))
