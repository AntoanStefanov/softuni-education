numbers = input().split()
string = input()

word = ''
for number in numbers:
    index = 0
    for digit in number:
        index += int(digit)

    while True:
        if index >= len(string):
            index -= len(string)
        word += string[index]
        string = string.replace(string[index], '', 1)
        break
print(word)
