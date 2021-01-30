import re


data = input()

regex = r"(?P<day>\d{2})(?P<separator>[\./-])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"


dates = re.finditer(regex, data)

for date in dates:
    date = date.groupdict()
    print(f"Day: {date['day']}, Month: {date['month']}, Year: {date['year']}")
