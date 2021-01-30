# import re


# data = input()

# regex = r"((?<=^_)|(?<=\s_))[A-Za-z\d]+\b"


# variables = [variable.group() for variable in re.finditer(regex, data)]

# print(",".join(variables))


import re


regex = r'\b_([a-zA-Z0-9]+)\b'


data = input()

# Връща всички групи , ако е повече от една с tuples, иначе си е в лист.
variables = re.findall(regex, data)

print(','.join(variables))
