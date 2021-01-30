#My solution
def encrypted(text):
    encrypted = ''

    for char in text:
        char = ord(char) + 3
        encrypted += chr(char)
    return encrypted


text = input()

print(encrypted(text))


line = input()
for ch in line:
    print(chr(ord(ch) + 3), end='')
