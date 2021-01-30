# def reversed_word(string):
#     return string[::-1]


# words = []
# while True:
#     command = input()
#     if command == "end":
#         break
#     words.append(command)

# for word in words:
#     print(f"{word} = {reversed_word(word)}")


#### My solution ###

while True:
    word = input()
    if word == "end":
        break
    reversed_word = word[::-1]
    print(f"{word} = {reversed_word}")
