# import re


# numbers = []
# line = input()
# regex = r"\d+"

# while line:

#     match = re.findall(regex, line)
#     if match:
#         # Разопакова [['22', '45']] , като ['22', '45'] extend
#         numbers.extend(match)

#     line = input()
# # Unpacking
# print(*numbers, sep=" ")
# # Join
# #print(" ".join(numbers))


import re

regex = r'\d+'


while True:

    sentence = input()
    if not sentence:
        break
    numbers_in_sentence = re.findall(regex, sentence)

    for number in numbers_in_sentence:
        print(number, end=" ")
