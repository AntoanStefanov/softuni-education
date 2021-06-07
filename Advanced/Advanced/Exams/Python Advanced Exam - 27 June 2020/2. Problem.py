########### SECOND TIME #########
n = int(input())


def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


matrix = read_matrix(n)


def find_snake(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'S':
                return [r, c]


snake_position = find_snake(matrix)


def find_burrows(matrix):
    burrows_position = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'B':
                burrows_position.append([r, c])
    return burrows_position


burrows_position = find_burrows(matrix)


directions = {
    'left': [0, -1],
    'right': [0, 1],
    'down': [1, 0],
    'up': [-1, 0],
}


def check_position(row, col):
    return 0 <= row < n and 0 <= col < n


food_quantity = 0

while True:
    move = input()
    matrix[snake_position[0]][snake_position[1]] = '.'

    snake_position = [snake_position[0] +
                      directions[move][0], snake_position[1] + directions[move][1]]

    if check_position(snake_position[0], snake_position[1]):
        row, col = snake_position[0], snake_position[1]
        if matrix[row][col] == '*':
            food_quantity += 1
            if food_quantity == 10:
                matrix[row][col] = 'S'
                print('You won! You fed the snake.')
                break
        elif matrix[row][col] == 'B':
            matrix[row][col] = '.'
            if snake_position == burrows_position[0]:
                snake_position = burrows_position[1]
            else:
                snake_position = burrows_position[0]

        matrix[snake_position[0]][snake_position[1]] = 'S'

    else:
        print("Game over!")
        break

print(f'Food eaten: {food_quantity}')
for row in matrix:
    print(''.join(row))


########################################################################

n = int(input())


def read_matrix(n):
    matrix = []
    for _ in range(n):
        matrix.append(list(input()))
    return matrix


matrix = read_matrix(n)


def find_snake(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'S':
                return [r, c]


snake_row, snake_col = find_snake(matrix)


def find_burrows(matrix):
    burrows_position = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 'B':
                burrows_position.append([r, c])
    return burrows_position


burrows_position = find_burrows(matrix)

is_out_of_box = False
food_quantity = 0
has_won = False

while True:
    move = input()

    if move == 'left':
        if 0 <= snake_col - 1 < n:
            if matrix[snake_row][snake_col-1] == '*':
                food_quantity += 1
                if food_quantity == 10:
                    has_won = True
                matrix[snake_row][snake_col-1] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_col -= 1
            elif matrix[snake_row][snake_col-1] == '-':
                matrix[snake_row][snake_col-1] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_col -= 1
            elif matrix[snake_row][snake_col-1] == 'B':
                matrix[snake_row][snake_col] = '.'
                current_burrow = [snake_row, snake_col-1]
                if current_burrow == burrows_position[0]:
                    matrix[snake_row][snake_col-1] = '.'
                    snake_row, snake_col = burrows_position[1]
                    matrix[snake_row][snake_col] = 'S'
                elif current_burrow == burrows_position[1]:
                    matrix[snake_row][snake_col-1] = '.'
                    snake_row, snake_col = burrows_position[0]
                    matrix[snake_row][snake_col] = 'S'
        else:
            matrix[snake_row][snake_col] = '.'
            is_out_of_box = True
    elif move == 'down':
        if 0 <= snake_row + 1 < n:
            if matrix[snake_row + 1][snake_col] == '*':
                food_quantity += 1
                if food_quantity == 10:
                    has_won = True
                matrix[snake_row + 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_row += 1
            elif matrix[snake_row + 1][snake_col] == '-':
                matrix[snake_row + 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_row += 1
            elif matrix[snake_row + 1][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                current_burrow = [snake_row + 1, snake_col]
                if current_burrow == burrows_position[0]:
                    matrix[snake_row + 1][snake_col] = '.'
                    snake_row, snake_col = burrows_position[1]
                    matrix[snake_row][snake_col] = 'S'
                elif current_burrow == burrows_position[1]:
                    matrix[snake_row + 1][snake_col] = '.'
                    snake_row, snake_col = burrows_position[0]
                    matrix[snake_row][snake_col] = 'S'
        else:
            matrix[snake_row][snake_col] = '.'
            is_out_of_box = True
    elif move == 'up':
        if 0 <= snake_row - 1 < n:
            if matrix[snake_row - 1][snake_col] == '*':
                food_quantity += 1
                if food_quantity == 10:
                    has_won = True
                matrix[snake_row - 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_row -= 1
            elif matrix[snake_row - 1][snake_col] == '-':
                matrix[snake_row - 1][snake_col] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_row -= 1
            elif matrix[snake_row - 1][snake_col] == 'B':
                matrix[snake_row][snake_col] = '.'
                current_burrow = [snake_row - 1, snake_col]
                if current_burrow == burrows_position[0]:
                    matrix[snake_row - 1][snake_col] = '.'
                    snake_row, snake_col = burrows_position[1]
                    matrix[snake_row][snake_col] = 'S'
                elif current_burrow == burrows_position[1]:
                    matrix[snake_row - 1][snake_col] = '.'
                    snake_row, snake_col = burrows_position[0]
                    matrix[snake_row][snake_col] = 'S'
        else:
            matrix[snake_row][snake_col] = '.'
            is_out_of_box = True
    elif move == 'right':
        if 0 <= snake_col + 1 < n:
            if matrix[snake_row][snake_col+1] == '*':
                food_quantity += 1
                if food_quantity == 10:
                    has_won = True
                matrix[snake_row][snake_col+1] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_col += 1
            elif matrix[snake_row][snake_col+1] == '-':
                matrix[snake_row][snake_col+1] = 'S'
                matrix[snake_row][snake_col] = '.'
                snake_col += 1
            elif matrix[snake_row][snake_col+1] == 'B':
                matrix[snake_row][snake_col] = '.'
                current_burrow = [snake_row, snake_col+1]
                if current_burrow == burrows_position[0]:
                    matrix[snake_row][snake_col+1] = '.'
                    snake_row, snake_col = burrows_position[1]
                    matrix[snake_row][snake_col] = 'S'
                elif current_burrow == burrows_position[1]:
                    matrix[snake_row][snake_col+1] = '.'
                    snake_row, snake_col = burrows_position[0]
                    matrix[snake_row][snake_col] = 'S'
        else:
            matrix[snake_row][snake_col] = '.'
            is_out_of_box = True

    if is_out_of_box:
        print("Game over!")
        break
    if has_won:
        print("You won! You fed the snake.")
        break

print(f'Food eaten: {food_quantity}')

for row in matrix:
    print(''.join(row))
