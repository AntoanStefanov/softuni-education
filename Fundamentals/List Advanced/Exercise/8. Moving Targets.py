target_values = [int(n) for n in input().split()]

while True:

    command = input()

    if command == "End":
        break

    tokens = command.split()

    command = tokens[0]
    index = int(tokens[1])

    if command == "Shoot":
        power = int(tokens[2])

        if 0 <= index < len(target_values):
            if target_values[index] - power <= 0:
                target_values.pop(index)
            else:
                target_values[index] -= power

    elif command == "Add":
        value = int(tokens[2])

        if 0 <= index < len(target_values):
            target_values.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        radius = int(tokens[2])

        left_radius = index - radius
        right_radius = index + radius
        if left_radius >= 0 and right_radius < len(target_values):
            del target_values[left_radius:right_radius + 1]
        else:
            print("Strike missed!")

print("|".join(map(str, target_values)))

### With functions ###
# НЕ знам как се използват тия проклети функции


def shoot(index):
    power = int(tokens[2])

    if 0 <= index < len(target_values):
        if target_values[index] - power <= 0:
            target_values.pop(index)
        else:
            target_values[index] -= power


def add(index):

    value = int(tokens[2])

    if 0 <= index < len(target_values):
        target_values.insert(index, value)
    else:
        print("Invalid placement!")


def strike(index):
    radius = int(tokens[2])

    left_radius = index - radius
    right_radius = index + radius
    if left_radius >= 0 and right_radius < len(target_values):
        del target_values[left_radius:right_radius + 1]
    else:
        print("Strike missed!")


target_values = [int(n) for n in input().split()]


while True:

    command = input()

    if command == "End":
        break

    tokens = command.split()

    command = tokens[0]
    index = int(tokens[1])

    if command == "Shoot":
        shoot(index)

    elif command == "Add":
        add(index)

    elif command == "Strike":
        strike(index)

print("|".join(map(str, target_values)))
