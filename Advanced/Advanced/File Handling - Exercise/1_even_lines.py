import re


def replace_and_reverse_sentence(sentence):

    sentence = re.sub(r'[-,.!?]', '@', sentence)
    words = sentence.split()
    return ' '.join(words[::-1])


with open('text.txt', 'r') as file:
    sentences = file.readlines()
    for index, sentence in enumerate(sentences):
        if index % 2 == 0:
            edited_sentence = replace_and_reverse_sentence(sentence)
            print(edited_sentence)


# Note:
    # the only special characters or metacharacters inside a character class are:
    # the closing bracket ],
    # the backslash \,
    # the caret ^,
    # and the hyphen - (no need to escape if it's at the beginning or the end).
