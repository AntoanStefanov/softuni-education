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


n = int(input())
matrix = read_matrix(n)
player = find_player(matrix)
print(player)
