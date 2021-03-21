secret_message = input()

while True:
    command = input()
    if command == 'Reveal':
        break
    info = command.split(':|:')
    command = info[0]
    if command == 'InsertSpace':
        index = int(info[1])
        secret_message = secret_message[:index] + \
            ' ' + secret_message[index:]
        print(secret_message)
    elif command == 'Reverse':
        substring = info[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, '', 1)
            substring = substring[::-1]
            secret_message += substring
            print(secret_message)
        else:
            print('error')
    elif command == 'ChangeAll':
        substring = info[1]
        replacement = info[2]
        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

print(f"You have a new text message: {secret_message}")
