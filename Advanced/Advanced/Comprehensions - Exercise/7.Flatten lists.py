# flatten_lists_strings = [l.split() for l in input().split('|')]
# flatten_lists_strings.reverse()
# [print(el, end=' ') for l in flatten_lists_strings for el in l]

[print(el, end=' ') for l in input().split('|')[::-1] for el in l.split()]
