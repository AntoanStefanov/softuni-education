enrypted_message = input()


while True:
    data = input()

    if data == 'Decode':
        break

    data = data.split('|')

    command = data[0]

    if command == 'Move':
        number_of_letters = int(data[1])
        substring_to_move = enrypted_message[:number_of_letters]
        left_substring = enrypted_message[number_of_letters:]
        enrypted_message = left_substring + substring_to_move
    elif command == 'Insert':
        index = int(data[1])
        value = data[2]
        first_part = enrypted_message[:index]
        second_part = enrypted_message[index:]
        enrypted_message = first_part + value + second_part

    elif command == 'ChangeAll':
        substring = data[1]
        replacement = data[2]
        enrypted_message = enrypted_message.replace(substring, replacement)
print(f"The decrypted message is: {enrypted_message}")
