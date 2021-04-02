rows = int(input())
columns = rows

commands = input().split()


def create_matrix(rows):
    matrix = []
    for row in range(rows):
        matrix.append(input().split())
    return matrix


matrix = create_matrix(rows)

miner_position = None
all_coals = 0
for row in range(rows):
    for column in range(columns):
        if matrix[row][column] == 's':
            miner_row = row
            miner_column = column
        if matrix[row][column] == 'c':
            all_coals += 1


collected_coals = 0
game_over = False
for direction in commands:

    if direction == 'left':
        if miner_column - 1 >= 0:
            miner_column -= 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    elif direction == 'up':
        if miner_row-1 >= 0:
            miner_row -= 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True
    elif direction == 'right':
        if miner_column+1 < columns:
            miner_column += 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    elif direction == 'down':
        if miner_row+1 < rows:
            miner_row += 1
            if matrix[miner_row][miner_column] == 'c':
                matrix[miner_row][miner_column] = '*'
                collected_coals += 1
            elif matrix[miner_row][miner_column] == 'e':
                game_over = True

    if game_over:
        print(f"Game over! ({miner_row}, {miner_column})")
        break
    if collected_coals == all_coals:
        print(f"You collected all coals! ({miner_row}, {miner_column})")
        break
else:
    print(f"{all_coals - collected_coals} coals left. ({miner_row}, {miner_column})")
