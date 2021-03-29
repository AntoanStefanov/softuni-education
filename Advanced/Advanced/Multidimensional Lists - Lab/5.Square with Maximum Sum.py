rows, columns = [int(x) for x in input().split(', ')]


matrix = []
for row in range(rows):
    columns_elements = [int(x) for x in input().split(', ')]
    matrix.append(columns_elements)

max_square = 0

for row in range(rows):
    current_row = row
    if current_row == len(matrix) - 1:
        continue
    next_row = row + 1

    for col in range(columns):
        # All pairs of the row
        if col == len(matrix[row]) - 1:
            continue
        current_value = matrix[current_row][col]
        next_col = col + 1
        next_value = matrix[current_row][next_col]

        next_row_current_value = matrix[next_row][col]
        next_row_next_value = matrix[next_row][next_col]

        square_sum = current_value + next_value + \
            next_row_current_value + next_row_next_value

        if square_sum > max_square:
            square = [[current_value, next_value], [
                next_row_current_value, next_row_next_value]]
            max_square = square_sum

for row in square:
    print(*row)
print(max_square)
