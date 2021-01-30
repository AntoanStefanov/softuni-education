cards = input().split(" ")

number_of_shuffles = int(input())

middle = len(cards) // 2


for shuffle in range(number_of_shuffles):

    current_shuffle = zip(cards[:middle], cards[middle:])

    cards.clear()

    for pair in current_shuffle:
        cards.extend(pair)


print(cards)


########## OR ############


cards = input().split()
number_of_shuffles = int(input())

middle = len(cards) // 2


for shuffle in range(number_of_shuffles):
    new_cards = []
    first_half = cards[:middle]
    second_half = cards[middle:]
    for card in range(len(first_half)):
        new_cards.append(first_half[card])
        new_cards.append(second_half[card])
    cards = new_cards
print(cards)


######### OR #########

cards = input().split()
number_of_shuffles = int(input())

new_deck = []
middle = len(cards) // 2

for shuffle in range(number_of_shuffles):
    for index in range(middle):
        first_card = cards[index]
        second_card = cards[index + middle]
        new_deck.append(first_card)
        new_deck.append(second_card)
    cards = new_deck
    new_deck = []
print(cards)
