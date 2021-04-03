string = input()

while True:
    data = input()

    if data == 'Done':
        break

    data = data.split()
    command = data[0]

    if command == 'Change':
        char_to_replace = data[1]
        replace_with = data[2]
        string = string.replace(char_to_replace, replace_with)
        print(string)
    elif command == 'Includes':
        str_to_check = data[1]
        if str_to_check in string:
            print('True')
        else:
            print('False')

    elif command == 'End':
        str_to_check = data[1]
        print(string.endswith(str_to_check))

    elif command == 'Uppercase':
        # Make all Uppercase and print it
        string = string.upper()
        print(string)
    elif command == 'FindIndex':
        char_to_find_index_to = data[1]  # the first one
        print(string.index(char_to_find_index_to))

    elif command == 'Cut':
        start_index = int(data[1])
        length = int(data[2])
        string = string[start_index: start_index + length]
        print(string)
