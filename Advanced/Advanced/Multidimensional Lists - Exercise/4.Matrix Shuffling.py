rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

print(matrix)


while True:
    data = input()

    if data == 'END':
        break

    data = data.split()

    command = data[0]

    if command == 'swap':
        if len(data) == 5:  # swap index1 index2 index3 index4
            pass
            # TODO check if indeces are valid
            first_row_index, first_col_index, second_row_index, second_col_index = data[1:]

            first_row_index = int(first_row_index)
            first_col_index = int(first_col_index)
            second_row_index = int(second_row_index)
            second_col_index = int(second_col_index)

            if 0 <= first_row_index < rows and 0 <= second_row_index < rows:
                if 0 <= first_col_index < cols and 0 <= second_col_index < cols:
                    # TODOpass
                    matrix[first_row_index][first_col_index], matrix[second_row_index][second_col_index] = matrix[
                        second_row_index][second_col_index], matrix[first_row_index][first_col_index]

                    print()
                else:
                    print('Invalid input!')
            else:
                print('Invalid input!')

        else:
            print('Invalid input!')
    else:
        print('Invalid input!')
