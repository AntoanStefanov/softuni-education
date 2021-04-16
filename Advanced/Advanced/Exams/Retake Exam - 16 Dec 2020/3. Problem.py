def get_magic_triangle(n):
    matrix = []
    for r in range(1, n + 1):
        matrix.append(list('0' * r))
    matrix[0][0] = 1
    matrix[1][0] = 1
    matrix[1][1] = 1

    for row in range(2, n):
        for col in range(0, row + 1):
            if col == 0:
                matrix[row][col] = 1
            elif col == row:
                matrix[row][col] = 1
            else:
                matrix[row][col] = matrix[row - 1][col - 1] + \
                    matrix[row - 1][col]
    return matrix


get_magic_triangle(6)
