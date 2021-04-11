def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result


print(multiply(4, 5, 6, 1, 3))
