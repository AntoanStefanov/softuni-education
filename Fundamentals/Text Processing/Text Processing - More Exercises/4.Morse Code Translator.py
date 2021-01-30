def morse_code_info(letter):
    if letter == '.-':
        return 'A'
    if letter == '-...':
        return 'B'
    if letter == '-.-.':
        return 'C'
    if letter == '-..':
        return 'D'
    if letter == '.':
        return 'E'
    if letter == '..-.':
        return 'F'
    if letter == '--.':
        return 'G'
    if letter == '....':
        return 'H'
    if letter == '..':
        return 'I'
    if letter == '.---':
        return 'J'
    if letter == '-.-':
        return 'K'
    if letter == '.-..':
        return 'L'
    if letter == '--':
        return 'M'
    if letter == '-.':
        return 'N'
    if letter == '---':
        return 'O'
    if letter == '.--.':
        return 'P'
    if letter == '--.-':
        return 'Q'
    if letter == '.-.':
        return 'R'
    if letter == '...':
        return 'S'
    if letter == '-':
        return 'T'
    if letter == '..-':
        return 'U'
    if letter == '.--':
        return 'W'
    if letter == '-..-':
        return 'X'
    if letter == '-.--':
        return 'Y'
    if letter == '--..':
        return 'Z'


morse_code = input()

words = morse_code.split(' | ')

code = []


def get_coded_word(word, words):
    if ' ' in word:
        word = word.strip()
        letters = word.split(' ')
        code.append(letters)
    else:
        letters = word
        code.append([letters])


for word in words:
    get_coded_word(word, words)


translated_code = []


def get_translated_word(word, code):
    translated_word = ''
    for letter in word:

        translated_letter = morse_code_info(letter)
        translated_word += translated_letter
    translated_code.append(translated_word)


for word in code:
    get_translated_word(word, code)


print(' '.join(translated_code))
