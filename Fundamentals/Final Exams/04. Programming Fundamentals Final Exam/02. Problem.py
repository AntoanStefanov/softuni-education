import re
threshold = 1
data = input()
pattern = r'\d'
digits = re.findall(pattern, data)
digits = [int(x) for x in digits]
for x in digits:
    threshold *= x


pattern = r'(::|\*\*)(?P<name>[A-Z][a-z]{2,})\1'
emojis_gen = re.finditer(pattern, data)  # generator


emojis_list = []
emojis_list = [e for e in emojis_gen]

print('Cool threshold:', threshold)

cool_emojis = []

for emoji in emojis_list:
    emoji_to_check = emoji.group('name')
    emoji_points = 0
    for char in emoji_to_check:
        emoji_points += ord(char)
    if emoji_points > threshold:
        cool_emojis.append(emoji.group())

print(f'{len(emojis_list)} emojis found in the text. The cool ones are:')
if len(cool_emojis):
    for e in cool_emojis:
        print(e)
