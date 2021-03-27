from collections import defaultdict
phone_book = defaultdict(str)

while True:
    data = input()
    if data.isdigit():
        number_of_searches = int(data)
        break

    name, number = data.split('-')

    phone_book[name] = number

for _ in range(number_of_searches):
    name = input()

    if name in phone_book:
        print(f'{name} -> {phone_book[name]}')
    else:
        print(f"Contact {name} does not exist.")
