# x = lambda a: a + 10  ||| variable = keyword argument: expression
# print(x(5))
# Commented beacuse pep-8 transofrms it as the below one..
# EQUALS TO


def y(a): return a + 10


print(y(5))


def fn(a): return lambda b: a + b # equals to fn = lambda a: lambda b: a + b


# Function defining another function inside,
# and the inner funtion has access to the outer function's scope(variables)
print(fn(1))
# that returns new lambda expression
# We can call the inner function
print(fn(1)(2))
# Which evaluate the expression a + b

# Closure structure means:
# Defined funtion in outer function's body. 

# Lambda can take multiple parameters