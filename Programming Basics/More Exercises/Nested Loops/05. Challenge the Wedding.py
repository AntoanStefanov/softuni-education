men = int(input())
women = int(input())
max_number_of_tables = int(input())
tables = 0
for man in range(1, men + 1):
    for woman in range(1, women + 1):
        if tables == max_number_of_tables:
            break
        print(f"({man} <-> {woman})", end=" ")
        tables += 1
    if tables == max_number_of_tables:
        break
