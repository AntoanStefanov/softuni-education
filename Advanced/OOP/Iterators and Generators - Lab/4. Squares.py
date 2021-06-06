def squares(n):
    num = 1
    while num <= n:
        yield num * num
        num += 1


print(list(squares(5)))

# Tuk ines fo reshi s for cikal, koe e za predpochitane ?