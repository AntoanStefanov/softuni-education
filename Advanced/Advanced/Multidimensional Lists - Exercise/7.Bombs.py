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

    if (row - 1 >= 0) and (column-1 >= 0):
        matrix[row-1][column-1] -= bomb_power
    if (row - 1 >= 0):
        matrix[row-1][column] -= bomb_power
    if (row - 1 >= 0) and (column+1 < columns):
        matrix[row-1][column+1] -= bomb_power
    if column + 1 < columns:
        matrix[row][column+1] -= bomb_power
    if (row + 1) < rows and (column+1 < columns):
        matrix[row+1][column+1] -= bomb_power
    if row + 1 < rows:
        matrix[row+1][column] -= bomb_power
    if row + 1 < rows and columns - 1 >= 0:
        matrix[row+1][column-1] -= bomb_power
    if columns - 1 >= 0:
        matrix[row][column-1] -= bomb_power
    matrix[row][column] = 0
