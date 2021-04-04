rows, columns = [int(x) for x in input().split()]


matrix = []


for _ in range(rows):
    matrix.append(list(input()))


print(matrix)
