from sys import maxsize
rows, columns = [int(x) for x in input().split()]

matrix = []


for r in range(rows):
    row = [int(x) for x in input().split()]
    matrix.append(row)

# It gave 80/100 if you assign 0 as submatrix_sum !! So it means there were negative nums
submatrix_sum = None
submatrix = []

for n_row in range(rows - 2):
    for n_col in range(columns - 2):

        # first row
        current_value = matrix[n_row][n_col]
        second_value = matrix[n_row][n_col + 1]
        third_value = matrix[n_row][n_col + 2]

        first_row = [current_value, second_value, third_value]
        # second row
        second_row_current_value = matrix[n_row + 1][n_col]
        second_row_second_value = matrix[n_row + 1][n_col + 1]
        second_row_third_value = matrix[n_row + 1][n_col + 2]

        second_row = [second_row_current_value,
                      second_row_second_value, second_row_third_value]
        # third row
        third_row_current_value = matrix[n_row + 2][n_col]
        third_row_second_value = matrix[n_row + 2][n_col + 1]
        third_row_third_value = matrix[n_row + 2][n_col + 2]

        third_row = [third_row_current_value,
                     third_row_second_value, third_row_third_value]

        first_second_rows_sum = sum(first_row) + sum(second_row)
        total_current_sum = first_second_rows_sum + sum(third_row)

        if submatrix_sum is None or total_current_sum > submatrix_sum:

            submatrix_sum = total_current_sum
            submatrix = [
                first_row,
                second_row,
                third_row,
            ]

print(f'Sum = {submatrix_sum}')
for row in submatrix:
    print(*row)

# Second Time #

rows, columns = [int(x) for x in input().split()]
matrix = []
for r in range(rows):
    matrix.append([int(x) for x in input().split()])


matrix_max_sum = None


# -2 Защото квадрата си е 3х3 и няма смисъл да чеквам последните 2 реда защото излизат от матрицата
for row in range(rows - 2):
    # -2 Защото квадрата си е 3х3 и няма смисъл да чеквам последните 2 колони защото излизат от матрицата
    for column in range(columns - 2):
        # Element po element
        # first_row = [matrix[row][column], matrix[row]
        #              [column + 1], matrix[row][column + 2]]
        # second_row = [matrix[row + 1][column], matrix[row + 1]
        #               [column + 1], matrix[row + 1][column + 2]]
        # third_row = [matrix[row + 2][column], matrix[row + 2]
        #              [column + 1], matrix[row + 2][column + 2]]
        # celiq red 
        first_row = matrix[row][column: column + 3]
        second_row = [matrix[row + 1][column: column + 3]]
        third_row = [matrix[row + 2][column: column + 3]]

        current_matrix_sum = sum(first_row) + sum(second_row) + sum(third_row)
        
        if matrix_max_sum == None or current_matrix_sum > matrix_max_sum:
            matrix_max_sum = current_matrix_sum
            best_matrix = [first_row, second_row, third_row]

print(f'Sum = {matrix_max_sum}')
for row in best_matrix:
    print(' '.join([str(n) for n in row]))

### THIRD ###

SQUARE_SIZE = 3


def read_current_square(the_matrix, row_idx, col_idx, square_size=SQUARE_SIZE):
    square = []
    for num in range(square_size):
        square.append(the_matrix[row_idx + num][col_idx:col_idx + square_size])
    return square


def calculate_current_square_sum(square):
    total_square_sum = 0
    for current_row in square:
        total_square_sum += sum(current_row)
    return total_square_sum


matrix = []

(rows, cols) = map(int, input().split())

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

max_square_sum = -maxsize
square_with_max_sum = None

for row_index in range(rows - SQUARE_SIZE + 1):
    for col_index in range(cols - SQUARE_SIZE + 1):
        current_square = read_current_square(matrix, row_index, col_index)
        current_square_sum = calculate_current_square_sum(current_square)
        if current_square_sum > max_square_sum:
            max_square_sum = current_square_sum
            square_with_max_sum = current_square

print(f"Sum = {max_square_sum}")
[print(*row, sep=" ") for row in square_with_max_sum]


################################################################

def read_matrix():
    n, m = map(int, input().split())
    return [[int(x) for x in input().split()] for _ in range(n)]


def get_squares(matrix, n):
    sums_squres_map = {}
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    for i in range(rows_count-n+1):
        for j in range(cols_count-n+1):
            square = [matrix[row][j:j+n] for row in range(i, i+n)]
            square_sum = get_matrix_sum(square)
            sums_squres_map[(i, j)] = square_sum
    return sums_squres_map


def get_matrix_sum(matrix):
    return sum(sum(matrix[i]) for i in range(len(matrix)))


def get_top_point_and_sum_of_max_square(sums_squres_map):
    for top_point, square_sum in sorted(sums_squres_map.items(), key=lambda x: -x[1]):
        return top_point, square_sum
    return 0, 0


def fmt_output(matrix, n, max_sum, max_square_top_point):
    nl = '\n'
    result = []
    i, j = max_square_top_point
    result.append(f'Sum = {max_sum}')
    for row in range(i, i+n):
        result.append(' '.join([str(x) for x in matrix[row][j:j+n]]))
    return nl.join(result)


def main() -> None:
    N = 3
    matrix = read_matrix()
    sums_squares_map = get_squares(matrix, N)
    max_square_top_point, max_sum = get_top_point_and_sum_of_max_square(
        sums_squares_map)
    print(fmt_output(matrix, N, max_sum, max_square_top_point))


main()
