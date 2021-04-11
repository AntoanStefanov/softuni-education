def rounding_number(*args):
    rounded_numbers = []
    for arg in args:
        rounded_numbers.append(round(arg))
    return rounded_numbers


numbers = [float(n) for n in input().split()]
rounded_numbers = rounding_number(*numbers)
print(rounded_numbers)

# With no *args
print([round(float(n)) for n in input().split()])
