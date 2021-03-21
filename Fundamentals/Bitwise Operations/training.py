import re

regex = r'\d+'

sentence = input()

while sentence:

    numbers_in_sentence = re.findall(regex, sentence)

    for number in numbers_in_sentence:
        print(number, end=" ")

    sentence = input()
