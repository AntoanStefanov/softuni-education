import re


#regex = r"w{3}\.[a-zA-Z\d-]+(\.[a-z]+)+"
# С look around (^|(?<=\s))w{3}\.[a-zA-Z\d-]+(\.[a-z]+)+($|(?=\s))
regex = r"(^|(?<=\s))w{3}\.[a-zA-Z\d-]+(\.[a-z]+)+($|(?=\s))"

while True:
    sentence = input()
    if sentence == "":
        break
    for link in re.finditer(regex, sentence):
        print(link.group())
