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
