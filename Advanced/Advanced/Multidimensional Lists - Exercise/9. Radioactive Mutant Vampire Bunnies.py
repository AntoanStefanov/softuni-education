rows, columns = [int(x) for x in input().split()]


matrix = []

for _ in range(rows):
    matrix.append(list(input()))

directions = input()

is_dead = False
has_won = False
player_current_row = None
player_current_column = None
for r in range(rows):
    for col in range(columns):
        if matrix[r][col] == 'P':
            player_current_row = r
            player_current_column = col

# When he collapse in a B , does his prevoius position is replaced with . ?
for step in directions:

    if step == 'U':
        if player_current_row - 1 >= 0:
            if matrix[player_current_row - 1][player_current_column] == 'B':
                is_dead = True
            else:
                matrix[player_current_row - 1][player_current_column] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_row -= 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'R':
        if player_current_column + 1 < len(columns):
            if matrix[player_current_row][player_current_column + 1] == 'B':
                is_dead = True
            else:
                matrix[player_current_row][player_current_column + 1] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_column += 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'D':
        if player_current_row + 1 < len(rows):
            if matrix[player_current_row + 1][player_current_column] == 'B':
                is_dead = True
            else:
                matrix[player_current_row + 1][player_current_column] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_row += 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True
    elif step == 'L':
        if player_current_column - 1 >= 0:
            if matrix[player_current_row][player_current_column - 1] == 'B':
                is_dead = True
            else:
                matrix[player_current_row][player_current_column - 1] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_column -= 1
        else:
            matrix[player_current_row][player_current_column] = '.'
            has_won = True

    B_positions = []

    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 'B':
                B_positions.append([row, column])

    for B in B_positions:
        B_row = B[0]
        B_column = B[1]

        if B_row - 1 >= 0:
            if matrix[B_row - 1][B_column] == 'P':
                is_dead = True
            matrix[B_row-1][B_column] = 'B'
        if B_column + 1 < columns:
            if matrix[B_row][B_column + 1] == 'P':
                is_dead = True
            matrix[B_row][B_column + 1] = 'B'
        if B_row + 1 < rows:
            if matrix[B_row + 1][B_column] == 'P':
                is_dead = True
            matrix[B_row + 1][B_column] = 'B'
        if B_column - 1 >= 0:
            if matrix[B_row][B_column - 1] == 'P':
                is_dead = True
            matrix[B_row][B_column - 1] = 'B'
    if has_won:
        break
    elif is_dead:
        break
for row in matrix:
    print(''.join(row))

if has_won:
    print(f'won: {player_current_row} {player_current_column}')
elif is_dead:
    print(f'dead: {player_current_row} {player_current_column}')
