matrix = []

for _ in range(8):
    matrix.append(list(input().split()))


for row in matrix:
    print(row)

queens_positions = []

for row in range(8):
    for col in range(8):
        if matrix[row][col] == 'Q':
            queens_positions.append([row, col])
print(queens_positions)
queens_capturing_king = []
for queen_position in queens_positions:

    is_king_captured = False
    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_col - 1 >= 0:  # LEFT #
        queen_col -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_col + 1 < 8:  # RIGHT #
        queen_col += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row - 1 >= 0:  # UP #
        queen_row -= 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row + 1 < 8:  # DOWN #
        queen_row += 1
        if matrix[queen_row][queen_col] == 'Q':
            break
        if matrix[queen_row][queen_col] == 'K':
            is_king_captured = True
            break
    if is_king_captured:
        queens_capturing_king.append(queen_position)
        continue

    queen_row = queen_position[0]
    queen_col = queen_position[1]
    while queen_row + 1 < 8 and queen_col + 1 < 8: # Primary Diagonal #



print(queens_capturing_king)
