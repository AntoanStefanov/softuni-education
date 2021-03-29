rows, columns = [int(x) for x in input().split()]


matrix = []


for r in range(rows):
    matrix.append(input().split())


counter = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        current_char = matrix[row][col]
        same_row_next_char = matrix[row][col + 1]
        next_row_current_char = matrix[row + 1][col]
        next_row_next_char = matrix[row + 1][col + 1]

        if current_char == same_row_next_char:
            if current_char == next_row_current_char:
                if current_char == next_row_next_char:
                    counter += 1

        # print(current_char, same_row_next_char)
        # print(next_row_current_char, next_row_next_char)
        # print()
print(counter)
