rows = int(input())
matrix = []

matrix = [
    [int(x) for x in input().split(', ')
     if int(x) % 2 == 0]
    for row in range(rows)
]


print(matrix)
