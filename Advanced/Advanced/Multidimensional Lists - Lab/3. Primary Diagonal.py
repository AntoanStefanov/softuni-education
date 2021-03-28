square_matrix_size = int(input())

matrix = []

for row in range(square_matrix_size):
    matrix.append([int(x) for x in input().split()])

total = 0

for row in range(square_matrix_size):
    column = row
    value = matrix[row][column]
    total += value

print(total)
