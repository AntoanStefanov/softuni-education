def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = input().split()
    return matrix


def find_player(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 'P':
                return [row, col]


def next_position(player, direction):
    row, col = player
    directions = {
        'left': (0, -1),
        'up': (-1, 0),
        'right': (0, 1),
        'down': (1, 0),
    }
    row += directions[direction][0]
    col += directions[direction][1]

    return [row, col]


def is_position_valid(position, n):
    row, col = position
    return 0 <= row < n and 0 <= col < n


coins = 0
n = int(input())
matrix = read_matrix(n)
player = find_player(matrix)
path = []
has_won = False
while True:
    direction = input()
    potential_player_position = next_position(player, direction)

    if is_position_valid(potential_player_position, n):
        row, col = potential_player_position
        if matrix[row][col] == 'X':
            coins //= 2
            break
        else:
            coins += int(matrix[row][col])

            path.append([row, col])
            player = row, col
            if coins >= 100:
                has_won = True
                break

    else:
        coins //= 2
        break

if has_won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print('Your path:')
for pos in path:
    print(pos)
