# rows, cols = [int(x) for x in input().split(', ')]

# matrix = []

# for r in range(rows):
#     elements = [int(x) for x in input().split(' ')]
#     matrix.append(elements)

# for col in range(cols):
#     column_sum = 0
#     for row in range(rows):
#         column_sum += matrix[row][col]
#     print(column_sum)


################################################################
# main loop is for columns, child loop for the rows
# matrix[0][0]
# matrix[1][0]
# matrix[2][0]

# matrix[0][1]
# matrix[1][1]
# matrix[2][1]

# ............

# transposition of a matrix (90 degrees)
# zip() returns a transpositioned matrix
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# print([el for el in zip(*matrix)])
# print(list(zip(*matrix)))
# transpositioned matrix = [
#    [1, 4, 7],
#    [2, 5, 8],
#    [3, 6, 9]
# ]
#
#########################
# SOLUTION WITH ZIP
rows, cols = [int(x) for x in input().split(', ')]

matrix = []

for r in range(rows):
    elements = [int(x) for x in input().split(' ')]
    matrix.append(elements)

transpositioned_matrix = zip(*matrix)

for tuple_of_elements_in_a_column in transpositioned_matrix:
    print(sum(tuple_of_elements_in_a_column))
