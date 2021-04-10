#### Easy Wayy ###

categories = input().split(', ')

n = int(input())

bunker = {category: [] for category in categories}

items_count = 0
total_quality = 0

for _ in range(n):
    data = input().split(' - ')
    category, item, *info = data
    quantity, quality = info[0].split(';')
    quantity = int(quantity.split(':')[1])
    quality = int(quality.split(':')[1])

    bunker[category].append(item)

    items_count += quantity
    total_quality += quality

print(f'Count of items: {items_count}')
print(f'Average quality: {total_quality / len(bunker):.2f}')

[print(f'{category} -> {", ".join(items)}')  # ", ".join(info) same as ", ".join(info.keys()). Also works
 for category, items in bunker.items()]


### Hard Way ### 

categories = input().split(', ')

n = int(input())

bunker = {category: {} for category in categories}


for _ in range(n):
    data = input().split(' - ')
    category, item, *info = data
    quantity, quality = info[0].split(';')
    quantity = int(quantity.split(':')[1])
    quality = int(quality.split(':')[1])

    bunker[category][item] = {'quantity': quantity, 'quality': quality}

items_count = 0
total_quality = 0
for category, info in bunker.items():
    for product, info1 in info.items():
        items_count += info1['quantity']
        total_quality += info1['quality']
print(f'Count of items: {items_count}')
print(f'Average quality: {total_quality / len(bunker):.2f}')

[print(f'{category} -> {", ".join(info.keys())}')  # ", ".join(info) same as ", ".join(info.keys()). Also works
 for category, info in bunker.items()]
