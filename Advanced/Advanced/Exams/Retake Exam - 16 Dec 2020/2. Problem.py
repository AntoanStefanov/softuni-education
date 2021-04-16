string = input()
n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))
n_commands = int(input())
commands = []
for _ in range(n_commands):
    commands.append(input())

player_row = None
player_col = None

for row in range(n):
    for col in range(n):
        if matrix[row][col] == 'P':
            player_row = row
            player_col = col




number_of_commands = len(commands) - 1
matrix[player_row][player_col] = '-'
for index, command in enumerate(commands):
    if command == 'up':
        if player_row - 1 >= 0:
            if matrix[player_row - 1][player_col] != '-':
                string += matrix[player_row - 1][player_col]
                matrix[player_row - 1][player_col] = '-'
            player_row = player_row - 1
        else:
            if string:
                string = string[:-1]
    elif command == 'right':
        if player_col + 1 < n:
            if matrix[player_row][player_col + 1] != '-':
                string += matrix[player_row][player_col + 1]
                matrix[player_row][player_col + 1] = '-'
            player_col = player_col + 1
        else:
            if string:
                string = string[:-1]
    elif command == 'down':
        if player_row + 1 < n:
            if matrix[player_row + 1][player_col] != '-':
                string += matrix[player_row + 1][player_col]
                matrix[player_row + 1][player_col] = '-'
            player_row = player_row + 1
        else:
            if string:
                string = string[:-1]
    elif command == 'left':
        if player_col - 1 >= 0:
            if matrix[player_row][player_col - 1] != '-':
                string += matrix[player_row][player_col - 1]
                matrix[player_row][player_col - 1] = '-'
            player_col = player_col - 1
        else:
            if string:
                string = string[:-1]
    if index == number_of_commands:
        matrix[player_row][player_col] = 'P'

print(string)
for row in matrix:
    print(''.join(row))
