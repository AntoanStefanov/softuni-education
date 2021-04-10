# square
n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break
    command, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)

    if 0 <= row < n and 0 <= col < n:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
print(matrix)
