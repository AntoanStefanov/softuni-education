# Comprehension
chars = input().split(', ')
ascii_values = {char: ord(char) for char in chars}
print(ascii_values)


# Same as standard syntax

my_dict = {}
for c in chars:
    my_dict[c] = ord(c)
print(my_dict)
