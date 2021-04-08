strings = input().split(', ')

info = [f'{string} -> {len(string)}'for string in strings]

print(', '.join(info))
