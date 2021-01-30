def replace_all(first, second):
    while first in second:
        second = second.replace(first, '')
    return second


first = input()
second = input()


print(replace_all(first, second))
