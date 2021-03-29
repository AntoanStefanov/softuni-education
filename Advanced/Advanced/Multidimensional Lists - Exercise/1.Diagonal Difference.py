square_matrix_size = int(input())

matrix = []

for r in range(square_matrix_size):
    row = [int(x) for x in input().split()]
    matrix.append(row)

primary_diagonal_sum = 0
for ij in range(square_matrix_size):
    primary_diagonal_sum += matrix[ij][ij]
secondary_diagonal_sum = 0
col = 0
for row in range(square_matrix_size-1, -1, -1):
    secondary_diagonal_sum += matrix[row][col]
    col += 1


print(abs(primary_diagonal_sum - secondary_diagonal_sum))
