import re

with open('words.txt', 'r') as file:
    searched_words = file.read().split()


words_occurrences = {}

with open('input.txt', 'r') as file:
    content = file.read().lower()
    all_words = re.findall(rf'[a-z\']+', content)
    for s_word in searched_words:
        s_word_occurances = all_words.count(s_word.lower())
        words_occurrences[s_word] = s_word_occurances

sorted_words_occurrences = sorted(
    words_occurrences.items(), key=lambda tup: -tup[1])

result = ''
for word, occurrences in sorted_words_occurrences:
    result += f'{word} - {occurrences}\n'

with open('output.txt', 'w') as file:
    file.write(result)
