rows = int(input())

flatten_matrix = []
matrix = []
for row in range(rows):
    elements = [int(x) for x in input().split(', ')]
    matrix.append(elements)

for sublist in matrix:
    for el in sublist:
        flatten_matrix.append(el)
print(flatten_matrix)
