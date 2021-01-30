n = int(input())

rows = []

for _ in range(n):

    row = input()

    rows.append(row)


for i, row in enumerate(rows):

    if 'k' in row:
        k_index = row.index('k')
        k_row_index = i
        last_right_row_index = len(row) - 1
        break


last_below_row_index = n - 1
last_above_row_index = 0
last_left_row_index = 0

steps = 0
is_out = False

if k_index - 1 < 0:
    is_out = True
    steps += 1


if k_index + 1 == last_right_row_index + 1:
    is_out = True
    steps += 1


if not is_out:
    for _ in range(50):
        if is_out:
            break
        if rows[k_row_index][k_index - 1] == ' ':

            while rows[k_row_index][k_index - 1] == ' ':

                row_list = list(rows[k_row_index])
                row_list[k_index - 1] = "#"
                new_row = "".join(row_list)

                rows[k_row_index] = new_row

                k_index = k_index - 1
                steps += 1
                if k_index == 0:  # ИЗлизане от ляво
                    steps += 1
                    is_out = True
                    break

        if rows[k_row_index][k_index + 1] == ' ':
            while rows[k_row_index][k_index + 1] == ' ':

                row_list = list(rows[k_row_index])

                row_list[k_index + 1] = "#"
                new_row = "".join(row_list)

                rows[k_row_index] = new_row

                k_index = k_index + 1
                steps += 1
                if k_index == last_right_row_index:  # ИЗлизане от дясно
                    steps += 1
                    is_out = True
                    break

        if rows[k_row_index - 1][k_index] == ' ':
            while rows[k_row_index - 1][k_index] == ' ':

                row_list = list(rows[k_row_index - 1])
                row_list[k_index] = "#"
                new_row = "".join(row_list)

                rows[k_row_index - 1] = new_row

                k_row_index = k_row_index - 1

                steps += 1
                if k_row_index == 0:  # ИЗлизане от горе
                    steps += 1
                    is_out = True
                    break

        if rows[k_row_index + 1][k_index] == ' ':
            while rows[k_row_index + 1][k_index] == ' ':

                row_list = list(rows[k_row_index + 1])
                row_list[k_index] = "#"
                new_row = "".join(row_list)

                rows[k_row_index + 1] = new_row

                k_row_index = k_row_index + 1

                steps += 1
                if k_row_index == last_below_row_index:  # ИЗлизане от долу
                    steps += 1
                    is_out = True
                    break


if is_out:
    print(f"Kate got out in {steps} moves")
else:
    print("Kate cannot get out")
