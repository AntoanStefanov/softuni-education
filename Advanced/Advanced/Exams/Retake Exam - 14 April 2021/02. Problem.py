def read_matrix(n):
    matrix = []
    for row in range(n):
        matrix.append([])
        matrix[row] = input().split()
    return matrix


def is_shot_valid(row, col, n):
    return 0 <= row < n and 0 <= col < n


def points(matrix, row, col):
    left_points = int(matrix[row][0])  # left
    up_points = int(matrix[0][col])  # up
    right_points = int(matrix[row][len(matrix[0]) - 1])  # right
    down_points = int(matrix[len(matrix) - 1][col])  # down
    return left_points + up_points + right_points + down_points


players = input().split(', ')
players_points = {players[0]: 501, players[1]: 501}
n = 7
matrix = read_matrix(n)
end_game = False
throws = 0
while True:
    throws += 1
    for player in players_points:
        shot = input().split(', ')
        row = int(shot[0][1:])
        col = int(shot[1][:-1])

        if is_shot_valid(row, col, n):
            if matrix[row][col] == 'D':
                points_made = points(matrix, row, col) * 2
            elif matrix[row][col] == 'T':
                points_made = points(matrix, row, col) * 3
            elif matrix[row][col] == 'B':
                end_game = True
                break
            else:
                points_made = int(matrix[row][col])

            players_points[player] -= points_made

            if players_points[player] <= 0:
                end_game = True
                break
    if end_game:
        print(f"{player} won the game with {throws} throws!")
        break
