def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = input().split()
    return matrix


def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'A':
                return [row, col]


def all_targets(matrix):
    tar = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'x':
                tar += 1
    return tar


def shoot(matrix, player, direction):
    n = len(matrix)
    row, col = player
    directions = {
        'left': (0, -1),
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
    }
    while True:
        if matrix[row][col] == 'x':
            matrix[row][col] = '.'
            return [row, col]
        row += directions[direction][0]
        col += directions[direction][1]

        if not is_position_valid(row, col, n):
            return None


def move(matrix, player, direction, steps):
    n = len(matrix)
    row, col = player
    directions = {
        'left': (0, -steps),
        'up': (-steps, 0),
        'right': (0, steps),
        'down': (steps, 0),
    }
    row += directions[direction][0]
    col += directions[direction][1]

    if not is_position_valid(row, col, n):
        return None
    if matrix[row][col] == 'x':
        return None
    if matrix[row][col] == '.':
        return [row, col]


def is_position_valid(row, col, n):
    return 0 <= row < n and 0 <= col < n


n = 5
matrix = read_matrix(n)
player = find_player(matrix)
n_commands = int(input())
shot_targets = []
total_targets = all_targets(matrix)
targets_on_map = total_targets

for _ in range(n_commands):
    data = input().split()
    command = data[0]
    direction = data[1]
    if command == 'move':
        steps = int(data[2])
        position = move(matrix, player, direction, steps)
        if position:
            matrix[player[0]][player[1]] = '.'
            player = position[0], position[1]
            matrix[player[0]][player[1]] = 'A'
    elif command == 'shoot':
        shot = shoot(matrix, player, direction)
        if shot:
            shot_targets.append(shot)
            total_targets -= 1
            if total_targets == 0:
                break

if total_targets == 0:
    print(f"Training completed! All {targets_on_map} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

if shot_targets:
    for target in shot_targets:
        print(target)
