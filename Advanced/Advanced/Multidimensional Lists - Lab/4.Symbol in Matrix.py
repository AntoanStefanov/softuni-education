rows_cols_number = int(input())


matrix = []

for row in range(rows_cols_number):
    elements_of_a_row = input()

    matrix.append(list(elements_of_a_row))

searched_symbol = input()
is_found = False
for row in range(rows_cols_number):
    for col in range(rows_cols_number):
        current_value = matrix[row][col]
        if current_value == searched_symbol:
            print(f'({row}, {col})')
            is_found = True
            break
    if is_found:
        break
else:
    print(f'{searched_symbol} does not occur in the matrix')
