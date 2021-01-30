number = int(input())
printing_number = 1
is_bigger_than_number = False
for rows in range(1, number + 1):
    for cols in range(1, rows + 1):
        print(printing_number, end=" ")
        printing_number += 1
        if printing_number > number:
            is_bigger_than_number = True
            break
    if is_bigger_than_number:
        break
    print()
