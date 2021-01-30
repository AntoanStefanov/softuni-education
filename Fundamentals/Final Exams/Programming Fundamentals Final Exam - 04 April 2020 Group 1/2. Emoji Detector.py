import re


regex = r"(:{2}|\*{2})[A-Z][a-z][a-z]+\1"  # r or \\

data = input()

threshold = 1
for char in data:
    if char.isdigit():
        threshold *= int(char)
print(f"Cool threshold: {threshold}")

emojis = re.finditer(regex, data)
all_emojis = {}
for emoji in emojis:
    emoji_letters = emoji.group()
    emoji_letters = emoji_letters[2:-2]

    emoji_threshold = 0
    for char in emoji_letters:
        emoji_threshold += ord(char)

    all_emojis[(emoji.group())] = emoji_threshold


print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")
for emoji, emoji_threshold in all_emojis.items():
    if emoji_threshold > threshold:
        print(emoji)
