
number_rows = int(input())
rows = []
for _ in range(number_rows):
    row = [int(r) for r in input().split()]
    rows.append(row)


attacked_squares = input().split()

destroyed_ships = 0

for attack in attacked_squares:
    row = int(attack[0])
    col = int(attack[2])
    if rows[row][col] > 0:
        rows[row][col] -= 1
        if rows[row][col] == 0:
            destroyed_ships += 1


print(destroyed_ships)
