
import re

data = input()

regex = r"(^|(?<=\s))[a-z0-9]+[\._-]?[a-z0-9]+@[a-z-]+(\.[a-z-]+)+"


emails = re.finditer(regex, data, re.IGNORECASE)

for email in emails:
    print(email.group())
