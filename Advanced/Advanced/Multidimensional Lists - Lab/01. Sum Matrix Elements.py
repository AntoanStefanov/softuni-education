rows, columns = [int(x) for x in input().split(', ')]

matrix = []
matrix_elements_sum = 0

for r in range(rows):
    row_elements = [int(x) for x in input().split(', ')]
    matrix_elements_sum += sum(row_elements)
    matrix.append(row_elements)
print(matrix_elements_sum)
print(matrix)
