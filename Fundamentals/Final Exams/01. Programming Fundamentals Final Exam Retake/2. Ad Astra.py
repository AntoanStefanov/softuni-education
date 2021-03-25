import re

string = input()
pattern = r'(#|\|)(?P<product>[a-zA-Z ]+)\1(?P<day>\d{2})\/(?P<month>\d{2})\/(?P<year>\d{2})\1(?P<calories>[0-9][0-9]{0,3}|10000)\1'


# for loop for iterator! re.finditer return iterator
iterator = re.finditer(pattern, string)


total_calories = 0
items = []


for match in iterator:
    product = match.group('product')
    day = match.group('day')
    month = match.group('month')
    year = match.group('year')
    calories = match.group('calories')
    items.append(
        f'Item: {product}, Best before: {day}/{month}/{year}, Nutrition: {calories}')
    total_calories += int(calories)

days = total_calories // 2000

print(f'You have food to last you for: {days} days!')

for info in items:
    print(info)
