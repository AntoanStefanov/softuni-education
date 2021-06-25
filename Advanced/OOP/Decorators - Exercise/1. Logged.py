def logged(func):
    def wrapper(*args):
        result = func(*args)
        return f'you called {func.__name__}{args}\nit returned {result}'
    return wrapper


@logged
def func(*args):  # Като декорираш функцията, замени името на ф-ята с wrappera
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
