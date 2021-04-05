rows = int(input())

flatten_matrix = []

matrix = [
    [int(x) for x in input().split(', ')]
    for row in range(rows)
]

flatten_matrix = [
    num
    for row in matrix
    for num in row
]
print(flatten_matrix)
