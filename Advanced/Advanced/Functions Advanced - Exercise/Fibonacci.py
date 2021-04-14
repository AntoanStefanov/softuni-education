# functools is a module, importing a decorator lru_cache
# lru_cache = LEAST RECENTLY USED CACHE, provides a one-line way to add memoization
# to your functions
# To use it: write @lru_cache before the function, in parentheses
# enter the number of values to cache, by default Python will cache
# the 128 most recently used values
from functools import lru_cache


def fibonacci1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci1(n - 1) + fibonacci1(n - 2)


for n in range(1, 11):
    # 1, 101 Зацикля, защото трябва да мине през всичко поотделно,
    # memoization is the solution for that
    print(n, ':', fibonacci1(n))


# Memoization
#   Idea: Cache values
#        Implemented Explicitly to see how it works.

fibonacci_cache = {}  # Store recent function calls


def fibonacci(n):
    # If we have cached the value, return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Otherwise we must compute the Nth term
    # First compute, cache it, return it
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # Cache the value and return it
    fibonacci_cache[n] = value
    return value


fibonacci(5)


# Built in Memoization
# Simpler, Cleaner, Fast

@lru_cache(maxsize=1000)
def fibonacci2(n):
    # Check that the input is a positive integer
    if type(n) != int:  # int
        raise TypeError("n must be a positive integer")
    if n < 1:  # positive
        raise ValueError("n must be a positive integer")

    # Compute the Nth term
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci2(n - 1) + fibonacci2(n - 2)


print(fibonacci2(0))
