first_number_end = int(input())
second_number_end = int(input())
third_number_end = int(input())

for i in range(1, first_number_end + 1):

    for j in range(2, second_number_end + 1):
        for j1 in range(2, j):
            if j % j1 == 0:
                break
        else:
            for x in range(2, third_number_end + 1):
                if i % 2 == 0 and x % 2 == 0:
                    print(f'{i} {j} {x}')
