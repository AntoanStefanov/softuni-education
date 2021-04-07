########################## LAMBDA #########


# x = lambda a: a + 10  ||| variable = keyword argument: expression
# print(x(5))
# Commented beacuse pep-8 transofrms it as the below one..
# EQUALS TO


def y(a): return a + 10


print(y(5))


def fn(a): return lambda b: a + b  # equals to fn = lambda a: lambda b: a + b


# Function defining another function inside,
# and the inner funtion has access to the outer function's scope(variables)
print(fn(1))
# We call the outer function and returns as a result the inner funtions.
# We can call the inner function
print(fn(1)(2))
# Which evaluate the expression a + b

# Closure structure means:
# Defined funtion in outer function's body.

# Lambda can take multiple parameters
# x = lambda a, b: a * b
# print(x(3, 4))

# full_name = lambda first, last: f'I am {first} {last}'
# result = full_name('Tony', 'Stefanov')
# print(result) # I am Tony Stefanov


filtered_nums = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
mapped_nums = list(map(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))  # x: x**2
print(filtered_nums)
print(mapped_nums)  # Тук се присвоява ретърна от lambdata


############## Packing Arguments *args * kwargs #################################


