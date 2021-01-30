
# number = int(input())
# for cols in range(1, number + 1):
#     for rows in range(1, cols + 1):
#         print("*", end="")
#     print()
# for lower_cols in range(number - 1, 0, -1):
#     for lower_rows in range(1, lower_cols + 1):
#         print("*", end="")
#     print()


n = int(input())


for row in range(1, n+1):
    print("*" * row)

for row in range(n-1, 0, -1):
    print('*' * row)
