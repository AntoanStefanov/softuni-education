first_integer = int(input())
second_integer = int(input())


def first_factorial(first_integer):
    factorial = 1
    for i in range(first_integer, 0, -1):
        factorial *= i
    return factorial


def second_factorial(second_integer):
    factorial = 1
    for i in range(second_integer, 0, -1):
        factorial *= i
    return factorial


def result(first_integer, second_integer):
    factorial_one = first_factorial(first_integer)
    factorial_two = second_factorial(second_integer)
    result = factorial_one / factorial_two
    return f"{result:.2f}"


res = result(first_integer, second_integer)

print(res)
