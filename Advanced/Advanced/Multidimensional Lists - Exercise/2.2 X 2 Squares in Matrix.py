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


# Second Time #
rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append(input().split())

squares = 0
# -1 Защото квадрата си е 2х2 и няма смисъл да чеквам последния 1 ред, защото излизат от матрицата
for row in range(rows - 1):
    # -1 Защото квадрата си е 2х2 и няма смисъл да чеквам последната 1 колона, защото излизат от матрицата
    for col in range(columns - 1):
        current_char = matrix[row][col]
        # Possible right
        if not current_char == matrix[row][col + 1]:
            continue

        # Possible diagonal
        if not current_char == matrix[row + 1][col + 1]:
            continue

        # Possible down
        if not current_char == matrix[row + 1][col]:
            continue

        squares += 1

print(squares)
