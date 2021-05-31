rows = int(input())
columns = rows
matrix = []
for _ in range(rows):
    row = list(input())
    matrix.append(row)


removed_K = 0
while True:
    most_K_attacks = 0
    position = []
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 'K':
                K_attacks = 0
                if (row - 2) >= 0 and (column - 1) >= 0:
                    if matrix[row-2][column-1] == 'K':
                        K_attacks += 1
                if (row - 2) >= 0 and (column + 1) < columns:
                    if matrix[row-2][column+1] == 'K':
                        K_attacks += 1
                if (row + 2) < rows and (column - 1) >= 0:
                    if matrix[row+2][column-1] == 'K':
                        K_attacks += 1
                if (row + 2) < rows and (column + 1) < columns:
                    if matrix[row+2][column+1] == 'K':
                        K_attacks += 1
                if (row - 1) >= 0 and (column - 2) >= 0:
                    if matrix[row-1][column-2] == 'K':
                        K_attacks += 1
                if (row - 1) >= 0 and (column + 2) < columns:
                    if matrix[row-1][column+2] == 'K':
                        K_attacks += 1
                if (row+1) < rows and (column - 2) >= 0:
                    if matrix[row+1][column-2] == 'K':
                        K_attacks += 1
                if (row+1) < rows and (column + 2) < columns:
                    if matrix[row+1][column+2] == 'K':
                        K_attacks += 1
                if K_attacks > most_K_attacks:
                    most_K_attacks = K_attacks
                    position = [row, column]
    if most_K_attacks:
        matrix[position[0]][position[1]] = '0'
        removed_K += 1
    else:
        print(removed_K)
        break


######### SECOND TIME #########

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))


def is_bound_valid(row, col):
    return 0 <= row < n and 0 <= col < n


def calculate_kills(matrix, row, col):
    kills = 0
    # Дефиниране на движението на коня, абстрактно(от което и да е място възможни ходове).
    # (-2, -1) - upleft (-2, +1) - upright | (+2, -1) - downleft (+2, +1) - downright
    # (+1, -2) - leftdown (-1, +2)- leftup | (1, -2) - rightup (1, 2) - rightdown и тн.
    rows = [-2, -2, 2, 2, 1, 1, -1, -1]
    cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for index in range(len(rows)):
        potential_row = row + rows[index]
        potential_col = col + cols[index]
        if is_bound_valid(potential_row, potential_col):
            potential_K_position = matrix[potential_row][potential_col]
            if potential_K_position == 'K':
                kills += 1
    return kills


removed_Ks = 0
most_K_kills = 0
most_K_kills_position = None
while True:
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                kills = calculate_kills(matrix, row, col)

                if kills > most_K_kills:
                    most_K_kills = kills
                    most_K_kills_position = [row, col]
    if most_K_kills:
        matrix[most_K_kills_position[0]][most_K_kills_position[1]] = 0
        removed_Ks += 1
        most_K_kills = 0
    else:
        break
print(removed_Ks)


##### THIRD TIME ####  TUPLES FOR CALCULATING KILLS ####

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(input()))


def is_bound_valid(row, col):
    return 0 <= row < n and 0 <= col < n


def calculate_kills(matrix, row, col):
    kills = 0
    K_potential_positions = [(-2, -1), (-2, 1), (2, -1),
                             (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2)]
    for potential_position in K_potential_positions:
        potential_row = row + potential_position[0]
        potential_col = col + potential_position[1]
        if is_bound_valid(potential_row, potential_col):
            potential_K_position = matrix[potential_row][potential_col]
            if potential_K_position == 'K':
                kills += 1
    return kills


removed_Ks = 0
most_K_kills = 0
most_K_kills_position = None
while True:
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                kills = calculate_kills(matrix, row, col)

                if kills > most_K_kills:
                    most_K_kills = kills
                    most_K_kills_position = [row, col]

    if most_K_kills:
        matrix[most_K_kills_position[0]][most_K_kills_position[1]] = 0
        removed_Ks += 1
        most_K_kills = 0
    else:
        break
print(removed_Ks)
