def absolute_values(*args):
    absolute_values = []
    for arg in args:
        absolute_values.append(abs(arg))
    return absolute_values


numbers = [float(n) for n in input().split()]

print(absolute_values(*numbers))

# Second way #

print(list(map(lambda str_num: abs(float(str_num)), input().split())))

# Third way # 

print([abs(float(n)) for n in input().split()])
