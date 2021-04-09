flatten_lists = [l for l in input().split('|')]
l1 = [l.split() for l in flatten_lists]
l1.reverse()
l2 = [int(el) for l in l1 for el in l]

print(' '.join([str(el) for el in l2]))
