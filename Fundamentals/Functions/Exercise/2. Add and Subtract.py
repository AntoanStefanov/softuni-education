first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a, b):
    sum_of_a_and_b = a + b
    return sum_of_a_and_b


def subtract(a, b):
    subtract_of_a_and_b = a - b
    return subtract_of_a_and_b


def sum_and_subtract(first_number, second_number, third_number):
    sum_of_a_and_b = sum_numbers(first_number, second_number)
    subtract_of_a_and_b = subtract(sum_of_a_and_b, third_number)
    return subtract_of_a_and_b


print(sum_and_subtract(first_number, second_number, third_number))
