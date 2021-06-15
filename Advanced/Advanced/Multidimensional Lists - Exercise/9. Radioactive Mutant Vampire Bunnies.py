rows, columns = [int(x) for x in input().split()]


matrix = []

for _ in range(rows):
    matrix.append(list(input()))

directions = input()

has_died = False
has_won = False
player_current_row = None
player_current_column = None
for r in range(rows):
    for col in range(columns):
        if matrix[r][col] == 'P':
            player_current_row = r
            player_current_column = col

for step in directions:

    if step == 'U':
        if player_current_row - 1 >= 0:
            if matrix[player_current_row - 1][player_current_column] == 'B':
                has_died = True
            else:
                matrix[player_current_row - 1][player_current_column] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_row -= 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'R':
        if player_current_column + 1 < columns:
            if matrix[player_current_row][player_current_column + 1] == 'B':
                has_died = True
            else:
                matrix[player_current_row][player_current_column + 1] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_column += 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'D':
        if player_current_row + 1 < rows:
            if matrix[player_current_row + 1][player_current_column] == 'B':
                has_died = True
            else:
                matrix[player_current_row + 1][player_current_column] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_row += 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'L':
        if player_current_column - 1 >= 0:
            if matrix[player_current_row][player_current_column - 1] == 'B':
                has_died = True
            else:
                matrix[player_current_row][player_current_column - 1] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_column -= 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True

    B_positions = []

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 'B':
                B_positions.append([row, column])

    for B in B_positions:
        B_row = B[0]
        B_column = B[1]

        if B_row - 1 >= 0:
            if matrix[B_row - 1][B_column] == 'P':
                has_died = True
                matrix[B_row-1][B_column] = 'B'
            if matrix[B_row - 1][B_column] == '.':
                matrix[B_row-1][B_column] = 'B'
        if B_column + 1 < columns:
            if matrix[B_row][B_column + 1] == 'P':
                has_died = True
                matrix[B_row][B_column + 1] = 'B'
            if matrix[B_row][B_column + 1] == '.':
                matrix[B_row][B_column + 1] = 'B'
        if B_row + 1 < rows:
            if matrix[B_row + 1][B_column] == 'P':
                has_died = True
                matrix[B_row + 1][B_column] = 'B'
            if matrix[B_row + 1][B_column] == '.':
                matrix[B_row + 1][B_column] = 'B'
        if B_column - 1 >= 0:
            if matrix[B_row][B_column - 1] == 'P':
                has_died = True
                matrix[B_row][B_column - 1] = 'B'
            if matrix[B_row][B_column - 1] == '.':
                matrix[B_row][B_column - 1] = 'B'
    if has_won:
        break
    elif has_died:
        break
for row in matrix:
    print(''.join(row))

if has_won:
    print(f'won: {player_current_row} {player_current_column}')
elif has_died:
    print(f'dead: {player_current_row} {player_current_column}')


###### SECOND TIME #########

rows, cols = [int(x) for x in input().split()]


def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(input()))
    return matrix


def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return [row, col]


def is_move_valid(row, col):
    return 0 <= row < rows and 0 <= col < cols


def player_move(row, col, direction):
    if direction == 'U':
        potential_row = row - 1
        potential_col = col
    elif direction == 'R':
        potential_col = col + 1
        potential_row = row
    elif direction == 'D':
        potential_row = row + 1
        potential_col = col
    elif direction == 'L':
        potential_col = col - 1
        potential_row = row

    if is_move_valid(potential_row, potential_col):
        matrix[row][col] = '.'
        if matrix[potential_row][potential_col] == 'B':
            return ('dead', potential_row, potential_col)
        matrix[potential_row][potential_col] = 'P'
        return potential_row, potential_col
    matrix[row][col] = '.'
    return 'won', row, col


def get_bunnies_indexes(matrix):
    bunnies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'B':
                bunnies.append([i, j])

    return bunnies


def mutate_bunny(matrix, row, col, is_dead):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for position in directions:
        potential_row = row + position[0]
        potential_col = col + position[1]
        if is_move_valid(potential_row, potential_col):
            if matrix[potential_row][potential_col] == 'P':
                is_dead = True
                dead_row, dead_col = potential_row, potential_col
            matrix[potential_row][potential_col] = 'B'
    if is_dead:
        return is_dead, dead_row, dead_col


def bunnies_mutate(matrix, is_dead):
    result = None
    bunnies = get_bunnies_indexes(matrix)
    for bunny in bunnies:
        res = mutate_bunny(matrix, bunny[0], bunny[1], is_dead)
        if res:
            result = res
    return result


matrix = read_matrix(rows)
player_position = find_player(matrix)
commands = list(input())
is_dead = False

for direction in commands:
    res = player_move(player_position[0], player_position[1], direction)

    res_1 = bunnies_mutate(matrix, is_dead)
    if res_1:
        is_dead, row, col = res_1

    if res[0] == 'dead':
        for row in matrix:
            print(''.join(row))
        print(f'dead: {res[1]} {res[2]}')
        break
    elif res[0] == 'won':
        for row in matrix:
            print(''.join(row))
        print(f'won: {res[1]} {res[2]}')
        break
    else:
        player_position[0], player_position[1] = res[0], res[1]

    if is_dead:
        for _ in matrix:
            print(''.join(_))
        print(f'dead: {row} {col}')
        break
