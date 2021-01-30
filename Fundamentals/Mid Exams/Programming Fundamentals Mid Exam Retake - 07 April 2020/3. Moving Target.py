targets = [int(value) for value in input().split()]


while True:
    data = input()
    if data == "End":
        break
    command, index, value = data.split()
    index = int(index)
    value = int(value)
    if command == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value

            if targets[index] <= 0:
                targets.remove(targets[index])

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif command == "Strike":
        left_radius = index - value
        right_radius = index + value

        if left_radius >= 0:
            if right_radius < len(targets):
                del targets[left_radius:right_radius + 1]
        else:
            print("Strike missed!")

targets = [str(value) for value in targets]
print("|".join(targets))
