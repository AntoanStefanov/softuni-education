

def decrypt_message(data, key):

    message = ''
    char_index = 0
    number_index = 0
    while char_index < len(data):
        number = key[number_index]
        char = data[char_index]
        message += chr(ord(char)-number)
        char_index += 1
        number_index += 1
        if number_index == len(key):
            number_index = 0
    return message


def get_type(message):

    left_index = message.find('&')
    right_index = message.rfind('&')
    found_type = message[left_index + 1:right_index]
    return found_type


def get_coordinates(message):

    left_index1 = message.find('<')
    right_index2 = message.rfind('>')
    coordinates = message[left_index1 + 1:right_index2]

    return coordinates


def main():
    key = [int(num) for num in input().split()]
    while True:
        data = input()
        if data == 'find':
            break
        message = decrypt_message(data, key)
        found_type = get_type(message)
        coordinates = get_coordinates(message)
        print(f"Found {found_type} at {coordinates}")


main()