import re


data = input()
# r = raw string  за да не escape-ваме \
pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"


names = re.findall(pattern, data)

print(' '.join(names))
