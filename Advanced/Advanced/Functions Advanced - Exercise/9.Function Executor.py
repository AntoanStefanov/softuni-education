def func_executor(*args):
    result_of_all_executed_functions = []
    for tupl in args:
        current_function = tupl[0]
        current_args = tupl[1]
        result_of_all_executed_functions.append(
            current_function(*current_args))
    return result_of_all_executed_functions


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))


######## SECOND TIME ######

def func_executor(*args):
    res = []
    for tuple in args:
        func = tuple[0]
        arguments = tuple[1]
        res.append(func(*arguments))
    return res


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2
