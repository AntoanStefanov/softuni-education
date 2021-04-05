rows = int(input())

flatten_matrix = []

matrix = [
    [int(x) for x in input().split(', ')]
    for row in range(rows)
]

flatten_matrix = [
    el
    for sublist in matrix
    for el in sublist
]
print(flatten_matrix)
