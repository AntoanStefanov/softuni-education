import re

letters_pattern = r'[a-zA-Z]'
punctuation_marks_pattern = r'[^a-zA-Z\s]'


def get_n(pattern, sentence):
    return len(re.findall(pattern, sentence))


with open('text.txt', 'r') as file:
    sentences = file.readlines()
    result = ''
    for index, sentence in enumerate(sentences, 1):
        n_letters = get_n(letters_pattern, sentence)
        n_punctuation_marks = get_n(punctuation_marks_pattern, sentence)
        result += f'Line {index}: {sentence.strip()} ({n_letters})({n_punctuation_marks})\n'

with open('output.txt', 'w') as file:
    file.write(result)
