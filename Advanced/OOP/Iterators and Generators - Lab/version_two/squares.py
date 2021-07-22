def squares(n):
    # number = 1
    # while number <= n:
    #     yield number ** 2
    #     number += 1

    # OR #
    for num in range(1, n + 1):
        yield num ** 2


print(list(squares(5)))
