def read_matrix(n):
    matrix = []

    for row1 in range(n):
        matrix.append([])
        for col1 in range(n):
            matrix[row1].append(0)
    return matrix


def read_and_deploy_bombs(matrix):
    n_bombs = int(input())
    bombs_positions = []
    for _ in range(n_bombs):
        row, col = '', ''
        bp = list(input().split())
        raw_row = bp[0]
        raw_col = bp[1]
        for char in raw_row:
            if char.isdigit():
                row += char
        for char in raw_col:
            if char.isdigit():
                col += char

        row = int(row)
        col = int(col)

        matrix[row][col] = '*'
        bombs_positions.append([row, col])

    return bombs_positions


def is_index_valid(row, col):
    return 0 <= row < n and 0 <= col < n


def check_neighbors(matrix, row, col, directions):
    for direction in directions:
        potential_row, potential_col = row + direction[0], col + direction[1]
        if is_index_valid(potential_row, potential_col):
            if not matrix[potential_row][potential_col] == '*':
                matrix[potential_row][potential_col] += 1


n = int(input())

matrix = read_matrix(n)
bombs_positions = read_and_deploy_bombs(matrix)

directions = [
    [0, -1],  # left
    [-1, -1],  # left up diagonal
    [-1, 0],  # up
    [-1, 1],  # up right diagonal
    [0, 1],  # right
    [1, 1],  # down right diagonal
    [1, 0],  # down
    [1, -1],  # down left diagonal
]


for bomb in bombs_positions:
    check_neighbors(matrix, bomb[0], bomb[1], directions)


for row in matrix:
    print(*row, sep=' ')
