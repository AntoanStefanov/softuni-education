# Тук логиката е достатъчно проста, за да не използваме функции

n = int(input())

train = [0] * n

while True:
    command = input()
    if command == "End":
        break

    tokens = command.split()
    command = tokens[0]

    if command == "add":
        people_to_add = int(tokens[1])
        train[-1] += people_to_add
    elif command == "insert":
        index = int(tokens[1])
        people_to_add = int(tokens[2])
        train[index] += people_to_add
    elif command == "leave":
        index = int(tokens[1])
        people_to_remove = int(tokens[2])
        train[index] -= people_to_remove
print(train)
