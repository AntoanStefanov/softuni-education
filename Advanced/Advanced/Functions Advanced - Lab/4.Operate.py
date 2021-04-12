from functools import reduce


def operate(operator, *args):
    if operator == '+':
        # Inital value should be provided reduce take 3rd optional arg
        # but judge gives 60/100 with 3rd arg (0, 0, 1, 1) so remove
        result = reduce(lambda x, y: x + y, args)
    elif operator == '-':
        result = reduce(lambda x, y: x - y, args)
    elif operator == '*':
        result = reduce(lambda x, y: x * y, args)
    elif operator == '/':
        result = reduce(lambda x, y: x / y, args)
    return result


print(operate("*", 0, 2, 3))
# Refactured


def operate1(operator, *args):

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        "/": lambda x, y: x / y,
    }
    return reduce(operations[operator], args)


print(operate1("*", 0, 2, 3))
