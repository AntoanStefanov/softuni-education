# words = input().split()


# for word in words:
#     char_code = ''
#     word_without_char_code = ''
#     for symbol in word:

#         if symbol.isdigit():
#             char_code += symbol
#         else:
#             word_without_char_code += symbol

#     letter = chr(int(char_code))

#     correct_word = list(letter + word_without_char_code)

#     correct_word[1], correct_word[-1] = correct_word[-1], correct_word[1]

#     valid_word = "".join(correct_word)

#     print(f"{valid_word}", end=" ")

### With Functions ###


def replace_char_code_to_letter(word):
    char_code = ''

    for symbol in word:
        if not symbol.isdigit():
            break

        char_code += symbol

    letter = chr(int(char_code))

    new_word = word.replace(char_code, letter)

    return new_word


def order_the_word(unordered_word):

    temp = list(unordered_word)

    temp[1], temp[-1] = temp[-1], temp[1]

    return "".join(temp)


def decipher(word):

    unordered_word = replace_char_code_to_letter(word)
    ordered_word = order_the_word(unordered_word)
    return ordered_word


words = input().split()

new_words = [decipher(word) for word in words]

print(" ".join(new_words))
