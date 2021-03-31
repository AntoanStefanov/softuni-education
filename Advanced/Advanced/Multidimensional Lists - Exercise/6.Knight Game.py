rows = int(input())
columns = rows
matrix = []
for _ in range(rows):
    row = list(input())
    matrix.append(row)


removed_K = 0
while True:
    most_K_attacks = 0
    position = []
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 'K':
                K_attacks = 0
                if (row - 2) >= 0 and (column - 1) >= 0:
                    if matrix[row-2][column-1] == 'K':
                        K_attacks += 1
                if (row - 2) >= 0 and (column + 1) < columns:
                    if matrix[row-2][column+1] == 'K':
                        K_attacks += 1
                if (row + 2) < rows and (column - 1) >= 0:
                    if matrix[row+2][column-1] == 'K':
                        K_attacks += 1
                if (row + 2) < rows and (column + 1) < columns:
                    if matrix[row+2][column+1] == 'K':
                        K_attacks += 1
                if (row - 1) >= 0 and (column - 2) >= 0:
                    if matrix[row-1][column-2] == 'K':
                        K_attacks += 1
                if (row - 1) >= 0 and (column + 2) < columns:
                    if matrix[row-1][column+2] == 'K':
                        K_attacks += 1
                if (row+1) < rows and (column - 2) >= 0:
                    if matrix[row+1][column-2] == 'K':
                        K_attacks += 1
                if (row+1) < rows and (column + 2) < columns:
                    if matrix[row+1][column+2] == 'K':
                        K_attacks += 1
                if K_attacks > most_K_attacks:
                    most_K_attacks = K_attacks
                    position = [row, column]
    if most_K_attacks:
        matrix[position[0]][position[1]] = '0'
        removed_K += 1
    else:
        print(removed_K)
        break
