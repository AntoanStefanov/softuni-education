matrix = []

for _ in range(8):
    matrix.append(list(input().split()))

queens_positions = []

for row in range(8):
    for col in range(8):
        if matrix[row][col] == 'Q':
            queens_positions.append([row, col])
queens_capturing_king = []
for queen_position in queens_positions:

    is_king_captured = False
    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_col - 1 >= 0:  # LEFT #
        queen_col -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_col + 1 < 8:  # RIGHT #
        queen_col += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row - 1 >= 0:  # UP #
        queen_row -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row + 1 < 8:  # DOWN #
        queen_row += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row - 1 >= 0 and queen_col + 1 < 8:  # Primary Diagonal Ascending #
        queen_row -= 1
        queen_col += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row + 1 < 8 and queen_col - 1 >= 0:  # Primary Diagonal Descending #
        queen_row += 1
        queen_col -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row + 1 < 8 and queen_col + 1 < 8:  # Secondary Diagonal Descending #
        queen_row += 1
        queen_col += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row - 1 >= 0 and queen_col - 1 >= 0:  # Secondary Diagonal Asceding #
        queen_row -= 1
        queen_col -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

if queens_capturing_king:
    for queen_capturing_king in queens_capturing_king:
        print(queen_capturing_king)
else:
    print('The king is safe!')


######## SECOND WAY ##########

def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = input().split()
    return matrix


def find_king_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'K':
                return [row, col]


def is_index_valid(r, c, n):
    return 0 <= r < n and 0 <= c < n


def is_queen_on_line(row, col, position):
    while True:
        potential_row, potential_col = position[0] + \
            row, position[1] + col
        if is_index_valid(potential_row, potential_col, n):
            row, col = potential_row, potential_col

            if matrix[potential_row][potential_col] == 'Q':
                return [potential_row, potential_col]
        else:
            return


n = 8
matrix = read_matrix(n)
king_position = find_king_position(matrix)
positions = [
    [0, -1],  # LEFT
    [-1, -1],  # LEFT UP
    [-1, 0],  # UP
    [-1, 1],  # RIGHT UP
    [0, 1],  # RIGHT
    [1, 1],  # RIGHT DOWN
    [1, 0],  # DOWN
    [1, -1],  # LEFT DOWN
]
queens = []
for position in positions:
    row, col = king_position[0], king_position[1]
    queen = is_queen_on_line(row, col, position)
    if queen:
        queens.append(queen)

if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")


##### DONCHO ####

def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = input().split()
    return matrix


def find_king_position(matrix):
    for row_index in range(len(matrix)):
        if 'K' in matrix[row_index]:
            column_index = matrix[row_index].index('K')
            return row_index, column_index


def in_range(value, max_value):
    return 0 <= value < max_value


def search_with_deltas(board, king, deltas):
    rows_count = len(board)
    column_count = len(board[0])
    delta_row, delta_col = deltas
    row_index, col_index = king

    while True:
        if board[row_index][col_index] == 'Q':
            return [row_index, col_index]
        row_index += delta_row
        col_index += delta_col

        if (not in_range(row_index, rows_count))\
                or (not in_range(col_index, column_count)):
            return None


def get_capturing_queens(board, king):
    deltas = [
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
    ]
    queens = [
        search_with_deltas(board, king, delta)
        for delta in deltas
    ]
    return [queen for queen in queens if queen is not None]


def print_result(queens):
    if queens:
        for queen in queens:
            print(queen)
    else:
        print('The king is safe!')


n = 8
board = read_matrix(n)
king = find_king_position(board)
queens = get_capturing_queens(board, king)
print_result(queens)
