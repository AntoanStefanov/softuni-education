cards = input().split(":")


deck = []

while True:

    command = input()

    if command == 'Ready':
        break

    data = command.split()

    command = data[0]

    if command == "Add":
        card = data[1]
        if card in cards:
            deck.append(card)
        else:
            print('Card not found.')

    elif command == 'Insert':
        card = data[1]
        index = int(data[2])
        if card in cards and 0 <= index < len(cards):
            deck.insert(index, card)
        else:
            print("Error!")

    elif command == 'Remove':
        card = data[1]
        if card in deck:
            deck.remove(card)
        else:
            print('Card not found.')
    elif command == 'Swap':
        card_1 = data[1]
        card_2 = data[2]
        card_1_index = deck.index(card_1)
        card_2_index = deck.index(card_2)
        deck[card_1_index], deck[card_2_index] = deck[card_2_index], deck[card_1_index]
    elif command == 'Shuffle':
        deck.reverse()

print(' '.join(deck))
