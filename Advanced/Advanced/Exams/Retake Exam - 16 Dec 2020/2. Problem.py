######### SECOND TIME #####


def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = list(input())
    return matrix


def read_directions():
    n_directions = int(input())
    directions = []
    for _ in range(n_directions):
        directions.append(input())
    return directions


def find_player_position(matrix):
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[0])):
            if matrix[row_index][col_index] == 'P':
                return [row_index, col_index]


def next_position(player_row, player_col, direction):
    moves = {
        'left': (0, -1),
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0)
    }
    player_row += moves[direction][0]
    player_col += moves[direction][1]
    return [player_row, player_col]


def is_position_valid(row, col, n):
    return 0 <= row < n and 0 <= col < n


def check_player_position(matrix, row, col):
    if not matrix[row][col] == '-':
        letter = matrix[row][col]
        matrix[row][col] = 'P'
        return letter
    return None


text = input()
n = int(input())
matrix = read_matrix(n)
directions = read_directions()
player_row, player_col = find_player_position(matrix)

for direction in directions:
    next_potential_position = next_position(player_row, player_col, direction)
    if is_position_valid(*next_potential_position, n):
        matrix[player_row][player_col] = '-'
        player_row, player_col = next_potential_position
        letter = check_player_position(matrix, player_row, player_col)
        if letter:
            text += letter
    else:
        if text:
            text = text[:-1]
print(text)
for row in matrix:
    print(*row, sep='')


####### FIRST TIME ########

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
