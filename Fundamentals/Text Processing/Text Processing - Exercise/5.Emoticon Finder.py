def emoticon_finder(text):

    emoticons = []

    for index, ch in enumerate(text):
        if ch == ":":
            if index + 1 < len(text):
                emoticon = f"{ch}{text[index + 1]}"
                emoticons.append(emoticon)

    return "\n".join(emoticons)


text = input()

print(emoticon_finder(text))
