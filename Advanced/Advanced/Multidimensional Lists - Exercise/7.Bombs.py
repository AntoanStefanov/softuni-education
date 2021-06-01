rows = int(input())
columns = rows

matrix = []

for r in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)


bombs_info = input().split()

bombs_coordinates = []
for bomb_info in bombs_info:
    bomb = [int(b) for b in bomb_info.split(',')]
    bombs_coordinates.append(bomb)


for bomb_coordinates in bombs_coordinates:
    row = bomb_coordinates[0]
    column = bomb_coordinates[1]
    bomb_power = matrix[row][column]
    if bomb_power <= 0:
        continue
    if (row - 1 >= 0) and (column-1 >= 0):
        if matrix[row-1][column-1] > 0:
            matrix[row-1][column-1] -= bomb_power
    if (row - 1 >= 0):
        if matrix[row-1][column] > 0:
            matrix[row-1][column] -= bomb_power
    if (row - 1 >= 0) and (column+1 < columns):
        if matrix[row-1][column+1] > 0:
            matrix[row-1][column+1] -= bomb_power
    if column + 1 < columns:
        if matrix[row][column+1] > 0:
            matrix[row][column+1] -= bomb_power
    if (row + 1) < rows and (column+1 < columns):
        if matrix[row+1][column+1] > 0:
            matrix[row+1][column+1] -= bomb_power
    if row + 1 < rows:
        if matrix[row+1][column] > 0:
            matrix[row+1][column] -= bomb_power
    if row + 1 < rows and column - 1 >= 0:
        if matrix[row+1][column-1] > 0:
            matrix[row+1][column-1] -= bomb_power
    if column - 1 >= 0:
        if matrix[row][column-1] > 0:
            matrix[row][column-1] -= bomb_power
    matrix[row][column] = 0


alive_cells = 0
sum_cells = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            sum_cells += el

print(f'Alive cells: {alive_cells}')
print(f"Sum: {sum_cells}")

for row in matrix:
    print(*row)

########### SECOND TIME WITH FUNCTIONS ###

n = int(input())


def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append([int(x) for x in input().split()])

    return matrix


def read_bombs_coordinates():
    bombs_coordinates = []
    for bomb in input().split():
        bomb_coordinates = [int(x) for x in bomb.split(',')]
        bombs_coordinates.append(bomb_coordinates)
    return bombs_coordinates


def is_cell_valid(matrix, row, col):
    return 0 <= row < n and 0 <= col < n and matrix[row][col] > 0


def explode(matrix, bomb_damage, row, col):
    potential_cells = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                       (1, 1), (1, 0), (1, -1), (0, -1)]

    for cell in potential_cells:
        cell_row = row + cell[0]
        cell_col = col + cell[1]
        if is_cell_valid(matrix, cell_row, cell_col):
            matrix[cell_row][cell_col] -= bomb_damage


def detonating_bomb(bomb_coordinates):
    row = bomb_coordinates[0]
    col = bomb_coordinates[1]
    bomb_damage = matrix[row][col]
    if bomb_damage > 0:
        explode(matrix, bomb_damage, row, col)
        matrix[row][col] = 0


def get_alive_cells_sum_and_count(matrix):
    sum_ = 0
    alive_cells = 0
    for row in matrix:
        for num in row:
            if num > 0:
                alive_cells += 1
                sum_ += num
    return sum_, alive_cells


def print_result(matrix, alive_cells_sum, alive_cells_count):
    print(f'Alive cells: {alive_cells_count}')
    print(f'Sum: {alive_cells_sum}')
    for row in matrix:
        print(' '.join([str(n) for n in row]))


matrix = read_matrix(n)
bombs_coordinates = read_bombs_coordinates()

for bomb_coordinates in bombs_coordinates:
    detonating_bomb(bomb_coordinates)

alive_cells_sum, alive_cells_count = get_alive_cells_sum_and_count(matrix)

print_result(matrix, alive_cells_sum, alive_cells_count)
