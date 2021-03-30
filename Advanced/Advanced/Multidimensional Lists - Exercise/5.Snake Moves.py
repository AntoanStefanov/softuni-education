from collections import deque
rows, columns = [int(x) for x in input().split()]

snake = deque(input())

matrix = [[] for _ in range(rows)]


for row in range(rows):
    for column in range(columns):
        next_element = snake.popleft()
        matrix[row].append(next_element)
        snake.append(next_element)
    if row % 2 == 1:
        matrix[row].reverse()
for row in matrix:
    print(''.join(row))
