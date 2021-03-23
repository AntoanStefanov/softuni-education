from collections import deque

liters = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill '):
        liters_to_add = int(command.split()[-1])
        liters += liters_to_add
    else:
        wanted_liters = int(command)
        if liters >= wanted_liters:
            print(f"{people.popleft()} got water")
            liters -= wanted_liters
        else:
            print(f"{people.popleft()} must wait")
print(f'{liters} liters left')

#####


liters = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break
    people.append(name)

while True:
    command = input()
    if command == 'End':
        break
    elif 'refill' in command:
        command = command.split()
        liters += int(command[1])
    else:
        wanted_liters = int(command)
        if liters >= wanted_liters:
            print(f"{people.popleft()} got water")
            liters -= wanted_liters
        else:
            print(f"{people.popleft()} must wait")
print(f'{liters} liters left')
