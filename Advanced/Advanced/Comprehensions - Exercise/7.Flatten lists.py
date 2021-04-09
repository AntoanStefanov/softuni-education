flatten_lists_strings = [l.split() for l in input().split('|')]
flatten_lists_strings.reverse()

flatten_lists_integers = [el for l in flatten_lists_strings for el in l]

print(' '.join([el for el in flatten_lists_integers]))
