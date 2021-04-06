rows, columns = [int(x) for x in input().split()]


matrix = []


for _ in range(rows):
    matrix.append(list(input()))

directions = input()

print(matrix)
print(directions)
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
    # Spread the bunnies first ?
    if step == 'U':
        if player_current_row - 1 >= 0:
            if matrix[player_current_row - 1][player_current_column] == 'B':
                is_dead = True
            else:
                matrix[player_current_row - 1][player_current_column] = 'P'
                matrix[player_current_row][player_current_column] = '.'
            player_current_row -= 1
        else:
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
            has_won = True

    for row in range(rows):
        for column in range(columns):

            if matrix[row][column] == 'B':
                if row - 1 >= 0:
                    if matrix[row - 1][column] == 'P':
                        is_dead = True
                    matrix[row - 1][column] = 'B'

                if column + 1 < columns:
                    if matrix[row][column + 1] == 'P':
                        is_dead = True
                    matrix[row][column + 1] = 'B'

                if row + 1 < rows:
                    if matrix[row + 1][column] == 'P':
                        is_dead = True
                    matrix[row + 1][column] = 'B'

                if column - 1 >= 0:
                    if matrix[row][column - 1] == 'P':
                        is_dead = True
                    matrix[row][column - 1] = 'B'

    if has_won:
        print(f'won: {player_current_row} {player_current_column}')
        break

    elif is_dead:
        print(f'dead: {player_current_row} {player_current_column}')
        break
