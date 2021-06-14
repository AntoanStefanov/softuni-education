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

n = 8


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


matrix = read_matrix(n)
king_position = find_king_position(matrix)
positions = [
    [0, -1],  # LEFT
    [-1, -1],  # LEFT UP
    [-1, 0],  # UP
    [-1, +1],  # RIGHT UP
    [0, +1],  # RIGHT
    [+1, +1],  # RIGHT DOWN
    [1, 0],  # DOWN
    [+1, -1],  # LEFT DOWN
]
queens = []
for position in positions:
    row, col = king_position[0], king_position[1]
    while True:
        potential_row, potential_col = position[0] + \
            row, position[1] + col

        if is_index_valid(potential_row, potential_col, n):
            if matrix[potential_row][potential_col] == 'Q':
                queens.append([potential_row, potential_col])
                break
            else:
                row, col = potential_row, potential_col
        else:
            break
if queens:
    for queen in queens:
        print(queen)
else:
    print("The king is safe!")
