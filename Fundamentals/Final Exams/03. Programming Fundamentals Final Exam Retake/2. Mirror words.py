import re
string = input()

pattern = r'(?P<sep>@|#)(?P<first_word>[A-Za-z]{3,})(?P=sep){2}(?P<second_word>[A-Za-z]{3,})(?P=sep)'


# Понеже finditer връща iterator въртим през него с цикъл
word_pairs = [match for match in re.finditer(pattern, string)]

if not word_pairs:
    print('No word pairs found!')
    print('No mirror words!')
else:
    mirror_words = []
    print(f'{len(word_pairs)} word pairs found!')
    for word_pair in word_pairs:
        pair = word_pair.groupdict()
        first_word = pair['first_word']
        second_word = pair['second_word']
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
    if mirror_words:
        print('The mirror words are:')
        print(', '.join(mirror_words))
    else:
        print('No mirror words!')
