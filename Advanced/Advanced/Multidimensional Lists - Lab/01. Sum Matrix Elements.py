# rows, columns = [int(x) for x in input().split(', ')]

# matrix = []
# matrix_elements_sum = 0

# for r in range(rows):
#     row_elements = [int(x) for x in input().split(', ')]
#     matrix.append(row_elements)

#     matrix_elements_sum += sum(row_elements)

# print(matrix_elements_sum)
# print(matrix)


##### Comprehensions ###################
import itertools
rows, columns = [int(x) for x in input().split(', ')]

matrix = [[int(x) for x in input().split(', ')] for r in range(rows)]
# Подаване като позиционен аргумент всеки един от редовете в матрицата *
# chain([1, 2, 3], [1, 2, 3]) -> [1, 2, 3, 1, 2, 3] Връзва във верига и връща chain_object
# След което може да се сумират sum([1, 2, 3, 1, 2, 3])~
# List with all elements in the matrix
# list_with_all_rows = list(itertools.chain(*matrix))
# print(list_with_all_rows)
matrix_sum = sum(itertools.chain(*matrix))
print(matrix_sum)
print(matrix)
