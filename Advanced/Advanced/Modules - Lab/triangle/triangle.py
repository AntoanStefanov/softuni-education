def first_half(n):
    for row in range(1, n+1):
        for column in range(1, row+1):
            print(column, end=' ')
        print()


def second_half(n):
    for row in range(n-1, 0, -1):
        for column in range(1, row+1):
            print(column, end=' ')
        print()


def triangle(n):
    first_half(n)
    second_half(n)


triangle(4)
