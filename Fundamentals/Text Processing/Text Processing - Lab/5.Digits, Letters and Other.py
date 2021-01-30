def all_digits(string):
    digits = ''
    for char in string:
        if char.isdigit():
            digits += char
    return digits


def all_letters(string):
    letters = ''
    for char in string:
        if char.isalpha():
            letters += char
    return letters


def others(string):
    others = ''
    for char in string:
        if not char.isdigit() and not char.isalpha():
            others += char
    return others


string = input()


print(all_digits(string))
print(all_letters(string))
print(others(string))
