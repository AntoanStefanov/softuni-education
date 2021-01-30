operator = input()
first_number = int(input())
second_number = int(input())


def calculation(first_number, second_number, operator):
    result = None  # Предефиниране на стойноста резулт , за да може ако дадат невалиден вход да не даде проблем  а да върне ноне
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number // second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    return result


print(calculation(first_number, second_number, operator))
