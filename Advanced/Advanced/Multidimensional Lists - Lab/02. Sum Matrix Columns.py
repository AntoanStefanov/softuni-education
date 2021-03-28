rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for r in range(rows):
    elements = [int(x) for x in input().split(' ')]
    matrix.append(elements)

for col in range(cols):
    column_sum = 0
    for row in range(rows):
        column_sum += matrix[row][col]
    print(column_sum)


################################################################
# main loop is for columns, child loop for the rows
# matrix[0][0]
# matrix[1][0]
# matrix[2][0]

# matrix[0][1]
# matrix[1][1]
# matrix[2][1]

# ............
