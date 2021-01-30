string = input()


dictionary = {}

for char in string:
    if char == " ":
        continue
    if char not in dictionary:
        dictionary[char] = 0
    dictionary[char] += 1


for char, occurrences in dictionary.items():
    print(f"{char} -> {occurrences}")
