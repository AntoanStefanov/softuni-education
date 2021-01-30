from sys import maxsize

max_number = -maxsize

command = input()

while command != "Stop":
    number = int(command)

    if number > max_number:
        max_number = number
    command = input()
else:
    print(max_number)
