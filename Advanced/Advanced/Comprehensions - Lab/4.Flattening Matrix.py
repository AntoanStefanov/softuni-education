rows = int(input())

flatten_matrix = []
matrix = []
for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

flatten_matrix = [
    el
    for sublist in matrix
    for el in sublist
]
print(flatten_matrix)
