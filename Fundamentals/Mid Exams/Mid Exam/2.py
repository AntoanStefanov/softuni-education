gifts = input().split()

while True:
    data = input()
    if data == 'No Money':
        break

    data = data.split()

    command = data[0]
    gift = data[1]

    if command == 'OutOfStock':
        if gift in gifts:
            for index, item in enumerate(gifts):
                if item == gift:
                    gifts[index] = 'None'
    elif command == 'Required':
        index = int(data[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command == 'JustInCase':
        gifts[-1] = gift

new_order = [gift for gift in gifts if not gift == 'None']
print(' '.join(new_order))
