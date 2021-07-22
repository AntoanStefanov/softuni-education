def values_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1

gen = values_gen(5)
print(gen)
for x in gen:
    print(x)
