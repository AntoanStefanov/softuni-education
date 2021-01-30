import re


data = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"


numbers = re.finditer(regex, data)

# for number in numbers:
#     print(number.group(), end=" ")

# OR #

numbers = [num.group() for num in numbers]
print(*numbers)
