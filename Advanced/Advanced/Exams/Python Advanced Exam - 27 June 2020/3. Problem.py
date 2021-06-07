def add(numbers: list, args, position):
    if position == 'beginning':
        numbers = list(args) + numbers
    elif position == 'end':
        numbers += list(args)
    return numbers


def remove_at_begginning(numbers: list, args):
    if args:
        elements_to_remove = args[0]
        while elements_to_remove:
            numbers.pop(0)
            elements_to_remove -= 1
    else:
        numbers.pop(0)

    return numbers


def remove_at_end(numbers: list, args):
    if args:
        elements_to_remove = args[0]
        while elements_to_remove:
            numbers.pop()
            elements_to_remove -= 1
    else:
        numbers.pop()

    return numbers


def list_manipulator(numbers: list, action=None, position=None, *args):
    if action == 'add':
        return add(numbers, args, position)
    elif action == 'remove':
        if position == 'beginning':
            return remove_at_begginning(numbers, args)
        elif position == 'end':
            return remove_at_end(numbers, args)


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
