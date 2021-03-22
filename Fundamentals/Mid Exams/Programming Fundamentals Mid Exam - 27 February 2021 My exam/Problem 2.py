array = input().split(' ')


while True:
    command = input()

    if command == 'end':
        break

    data = command.split()

    if data[0] == 'reverse':
        starting_index = int(data[2])
        count = int(data[4])
        ending_index = starting_index + count
        array[starting_index:ending_index] = reversed(
            array[starting_index:ending_index])
    if data[0] == 'sort':
        starting_index = int(data[2])
        count = int(data[4])
        ending_index = starting_index + count
        array[starting_index:ending_index] = sorted(
            array[starting_index:ending_index])
    if data[0] == 'remove':
        ending_index = int(data[1])
        del array[:ending_index]

print(', '.join(array))


# OR


sequence = input().split()


while True:
    command = input()
    if command == "end":
        break

    command = command.split()

    if 'reverse' in command:
        starting_index = int(command[2])
        count = int(command[4])
        ending_index = starting_index + count
        portion = sequence[starting_index:ending_index]
        del sequence[starting_index:ending_index]
        for number in portion:
            sequence.insert(starting_index, number)

    elif 'sort' in command:
        starting_index = int(command[2])
        count = int(command[4])
        ending_index = starting_index + count
        portion = sequence[starting_index:ending_index]
        portion.sort(reverse=True)
        del sequence[starting_index:ending_index]
        for number in portion:
            sequence.insert(starting_index, number)

    elif 'remove' in command:
        count = int(command[1])
        del sequence[:count]


print(*sequence, sep=", ")
