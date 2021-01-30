

# First time solving
gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()
    gift = command[1]
    if command[0] == "OutOfStock" and gift in gifts:
        for index, gift_in_list in enumerate(gifts):
            if gift == gift_in_list:
                gifts[index] = "None"
    if command[0] == "Required" and 0 <= int(command[2]) < len(gifts):
        gifts[int(command[2])] = gift

    if command[0] == "JustInCase":
        gifts[len(gifts) - 1] = command[1]
    command = input()

for gift in range(len(gifts) - 1, -1, -1):
    if "None" in gifts[gift]:
        gifts.remove(gifts[gift])

for index in range(len(gifts)):
    print(gifts[index], end=' ')


# Second time Solving

gifts = input().split()


while True:
    data = input()
    if data == "No Money":
        break
    data = data.split()
    command = data[0]
    gift = data[1]
    if command == 'OutOfStock':
        while gift in gifts:
            index = gifts.index(gift)
            gifts[index] = None
    elif command == "Required":
        index = int(data[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift
    elif command == 'JustInCase':
        gifts[-1] = gift

gifts = [gift for gift in gifts if not gift == None]

print(' '.join(gifts))
