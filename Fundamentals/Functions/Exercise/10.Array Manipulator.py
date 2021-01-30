from sys import maxsize


def exchange(array, index):
    return array[index + 1:] + array[:index + 1]


def get_max_even(array):
    max_even = -maxsize
    index = -1
    for i, num in enumerate(array):
        if num % 2 == 0:
            if num >= max_even:
                max_even = num
                index = i
    return index


def get_max_odd(array):
    max_odd = -maxsize
    index = -1
    for i, num in enumerate(array):
        if num % 2 == 1:
            if num >= max_odd:
                max_odd = num
                index = i
    return index


def get_min_even(array):
    min_even = maxsize
    index = -1
    for i, num in enumerate(array):
        if num % 2 == 0:
            if num <= min_even:
                min_even = num
                index = i
    return index


def get_min_odd(array):
    min_odd = maxsize
    index = -1
    for i, num in enumerate(array):
        if num % 2 == 1:
            if num <= min_odd:
                min_odd = num
                index = i
    return index


def get_count_first_even(array, count):
    temp_list = []
    counter = 0
    for num in array:
        if counter == count:
            break

        if num % 2 == 0:
            temp_list.append(num)
            counter += 1
    return temp_list


def get_count_first_odd(array, count):
    temp_list = []
    counter = 0
    for num in array:
        if counter == count:
            break

        if num % 2 == 1:
            temp_list.append(num)
            counter += 1
    return temp_list


def get_count_last_even(array, count):
    temp_list = []
    counter = 0
    for i in range(len(array) - 1, -1, -1):
        num = array[i]

        if counter == count:
            break

        if num % 2 == 0:
            temp_list.append(num)
            counter += 1
    temp_list.reverse()
    return temp_list


def get_count_last_odd(array, count):
    temp_list = []
    counter = 0
    for i in range(len(array)-1, -1, -1):
        num = array[i]

        if counter == count:
            break

        if num % 2 == 1:
            temp_list.append(num)
            counter += 1
    temp_list.reverse()
    return temp_list


numbers = input().split()
array = []
for number in numbers:
    array.append(int(number))

command_input = input()

while command_input != "end":
    tokens = command_input.split()
    command = tokens[0]

    if command == "exchange":
        index = int(tokens[1])
        if 0 <= index < len(array):
            array = exchange(array, index)
        else:
            print("Invalid index")
            command_input = input()
            continue

    elif command == "max":

        parity = tokens[1]
        index = -1

        if parity == "even":
            index = get_max_even(array)
        elif parity == "odd":
            index = get_max_odd(array)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command == "min":

        parity = tokens[1]
        index = -1

        if parity == "even":
            index = get_min_even(array)
        elif parity == "odd":
            index = get_min_odd(array)

        if index != -1:
            print(index)
        else:
            print("No matches")

    elif command == "first":
        count = int(tokens[1])

        if count > len(array):
            print("Invalid count")
            command_input = input()
            continue

        parity = tokens[2]
        res = []

        if parity == "even":
            res = get_count_first_even(array, count)
        elif parity == "odd":
            res = get_count_first_odd(array, count)

        print(res)

    elif command == "last":
        count = int(tokens[1])

        if count > len(array):
            print("Invalid count")
            command_input = input()
            continue

        parity = tokens[2]
        res = []

        if parity == "even":
            res = get_count_last_even(array, count)
        elif parity == "odd":
            res = get_count_last_odd(array, count)

        print(res)

    command_input = input()

print(array)
