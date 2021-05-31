from collections import deque

rows, columns = [int(x) for x in input().split()]

snake = deque(input())
matrix = []

for row in range(rows):
    matrix.append([])
    for column in range(columns):
        char = snake.popleft()
        matrix[row].append(char)
        snake.append(char)
    if row % 2 == 1:
        matrix[row].reverse()

for row in matrix:

    print(''.join(row))
