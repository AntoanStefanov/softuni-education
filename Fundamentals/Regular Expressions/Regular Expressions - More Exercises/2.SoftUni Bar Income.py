import re


regex = r'\%(?P<customer>[A-Z][a-z]+)\%[^|$%.]*\<(?P<product>\w+)\>[^|%$.]*\|(?P<count>\d+)\|[^|$%.]*?(?P<price>\d+\.?\d+)\$$'


total_price = 0

while True:
    info = input()

    if info == 'end of shift':
        break

    matches = re.finditer(regex, info)

    for match in matches:
        count = int(match.group('count'))
        price = float(match.group('price'))
        price = count * price
        print(f"{match.group('customer')}: {match.group('product')} - {price:.2f}")
        total_price += price

print(f"Total income: {total_price:.2f}")
