
password = input()


while True:
    command = input()

    tokens = command.split()
    command = tokens[0]

    if command == "Done":
        break
    elif command == "TakeOdd":
        raw_password = ''
        for index, char in enumerate(password):
            if index % 2 != 0:
                raw_password += char
        password = raw_password
        print(password)

    elif command == "Cut":
        index = int(tokens[1])
        length = int(tokens[2])
        substring = password[index:index+length]
        password = password.replace(substring, '', 1)
        print(password)
    elif command == "Substitute":
        substring = tokens[1]
        substitute = tokens[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
