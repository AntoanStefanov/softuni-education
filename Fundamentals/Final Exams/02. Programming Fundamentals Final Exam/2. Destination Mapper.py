import re

pattern = r'(=|\/)(?P<name>[A-Z][A-Za-z]{2,})\1'
info = input()


matches = re.finditer(pattern, info)  # matches is an iterator


destinations = []
points = 0

for m in matches:
    destination = m.group('name')

    destinations.append(destination)
    points += len(destination)


print(f'Destinations: {", ".join(destinations)}')

print(f'Travel Points: {points}')
