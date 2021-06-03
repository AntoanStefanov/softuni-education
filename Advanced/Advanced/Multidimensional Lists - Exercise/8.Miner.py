rows = int(input())
columns = rows

commands = input().split()


def create_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    return matrix


matrix = create_matrix(rows)

miner_position = None
all_coals = 0
for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == 's':
            miner_row = row
            miner_column = column
        if matrix[row][column] == 'c':
            all_coals += 1


collected_coals = 0
game_over = False
for direction in commands:

    if direction == 'left':
        if miner_column - 1 >= 0:
            miner_column -= 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    elif direction == 'up':
        if miner_row - 1 >= 0:
            miner_row -= 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True
    elif direction == 'right':
        if miner_column + 1 < columns:
            miner_column += 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    elif direction == 'down':
        if miner_row + 1 < rows:
            miner_row += 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    if game_over:
        print(f'Game over! ({miner_row}, {miner_column})')
        break
    if collected_coals == all_coals:
        print(f"You collected all coals! ({miner_row}, {miner_column})")
        break
else:
    print(f"{all_coals - collected_coals} coals left. ({miner_row}, {miner_column})")

################### SECOND TIME #######

n = int(input())
movements = input().split()


def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(input().split())
    return matrix


def get_all_coals(matrix):
    all_coals = 0
    for row in matrix:
        for character in row:
            if character == 'c':
                all_coals += 1
    return all_coals


def get_miner_position(matrix):
    position = None
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 's':
                position = [i, j]
    return position


def is_potential_position_valid(row, col):
    return 0 <= row < n and 0 <= col < n


def get_potential_position(row, col, direction):
    # Rechnik moje bi ? {'left': (0, -1)}
    if direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1
    elif direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1

    return row, col


def move(matrix, direction, miner_position):

    row, col = get_potential_position(
        miner_position[0], miner_position[1], direction)

    if is_potential_position_valid(row, col):
        miner_position[0], miner_position[1] = row, col
        row = miner_position[0]
        col = miner_position[1]
        if matrix[row][col] == 'e':
            return -1
        elif matrix[row][col] == 'c':
            matrix[row][col] = '*'


matrix = read_matrix(n)
miner_position = get_miner_position(matrix)

for movement in movements:
    if move(matrix, movement, miner_position) == -1:
        print(f'Game over! ({miner_position[0]}, {miner_position[1]})')
        break
else:
    left_coals = get_all_coals(matrix)
    if left_coals:
        print(
            f'{left_coals} coals left. ({miner_position[0]}, {miner_position[1]})')
    else:
        print(
            f'You collected all coals! ({miner_position[0]}, {miner_position[1]})')


