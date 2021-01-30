from sys import maxsize

min_number = maxsize

command = input()

while command != "Stop":
    number = int(command)

    if number < min_number:
        min_number = number
    command = input()
else:
    print(min_number)
