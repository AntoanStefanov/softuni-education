import re

letters_pattern = r'[a-zA-Z]'
punctuation_marks_pattern = r'[^a-zA-Z\s]'


def get_n(pattern, sentence):
    return len(re.findall(pattern, sentence))


def prepare_output(sentences):
    output = ''
    for index, sentence in enumerate(sentences, 1):
        n_letters = get_n(letters_pattern, sentence)
        n_punctuation_marks = get_n(punctuation_marks_pattern, sentence)
        output += f'Line {index}: {sentence} ({n_letters})({n_punctuation_marks})\n'
    return output[:-1]


def start_program():
    with open('text.txt', 'r') as file:
        sentences = file.read().split('\n')
        output = prepare_output(sentences)

    with open('output.txt', 'w') as file:
        file.write(output)


start_program()
