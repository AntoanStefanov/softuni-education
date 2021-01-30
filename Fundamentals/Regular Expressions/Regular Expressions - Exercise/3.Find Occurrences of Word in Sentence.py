import re


text = input()
word = input()
pattern = rf'\b{word}\b' # or f'\\b{word}\\b'

list_of_occurences = re.findall(pattern, text, re.IGNORECASE)


print(len(list_of_occurences))
