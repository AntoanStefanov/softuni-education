# square
n = int(input())

matrix = [[int(num) for num in input().split()] for _ in range(n)]

print(matrix)

while True:
    command = input()
    if command == "END":
        break
    command, row, col, value = command.split()
    row = int(row)
    col = int(col)
    value = int(value)