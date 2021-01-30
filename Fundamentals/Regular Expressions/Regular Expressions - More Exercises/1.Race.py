import re

regex = r'\d?[A-Z]?[a-z]?'

result = {}

participants = input().split(', ')


while True:
    sentence = input()
    if sentence == 'end of race':
        break
    needed_els = ''
    for info in re.finditer(regex, sentence):
        needed_els += info.group()
    distance = 0
    name = ''
    for symbol in needed_els:
        if symbol.isdigit():
            distance += int(symbol)
        else:
            name += symbol
    if name in participants:
        if name in result.keys():
            result[name] += distance
        else:
            result[name] = distance


sorted_result = dict(sorted(result.items(), key=lambda x: -x[1]))
place = 0
for man, km in sorted_result.items():
    place += 1
    if place == 1:
        prefix = 'st'
    elif place == 2:
        prefix = 'nd'
    elif place == 3:
        prefix = 'rd'
    print(f'{place}{prefix} place: {man}')
    if place == 3:
        break
