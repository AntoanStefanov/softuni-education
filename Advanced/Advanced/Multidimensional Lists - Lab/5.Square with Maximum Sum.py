rows, columns = [int(x) for x in input().split(', ')]
print(rows, columns)


matrix = []
for row in range(rows):
    columns_elements = [int(x) for x in input().split(', ')]
    matrix.append(columns_elements)
print(matrix)


for row in range(rows):
    current_row = row
    next_row = row + 1
    print(matrix[row])
    for col in range(columns):
        # All pairs of the row
        if col == len(matrix[row]) - 1:
            continue
        current_value = matrix[current_row][col]
        next_col = col + 1
        next_value = matrix[current_row][next_col]
        print(current_value, next_value)
        # TODO All pairs of row + 1 