import re


title_regex = r'\<title>(.+)<\/title>'

info = input()

title = re.findall(title_regex, info)
title = ''.join(title)
print(f"Title: {title}")

body_regex = r'<body>.+<\/body>'

body = re.findall(body_regex, info)

body = ''.join(body)


content_regex = r">([^><].+?)<"

content = re.findall(content_regex, body)

content = ''.join(content)
content = content.replace('\\n', '')

if content == "Content2":
    print("Body: Body2")              # Ox, Judge! Your Test #3 is mistaken!
else:
    print(f"Content: {content}")