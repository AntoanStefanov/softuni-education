from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card_name: str):
        if card_name == '':
            raise ValueError("Card cannot be an empty string!")
        card = self.find(card_name)
        self.cards.remove(card)
        self.count -= 1

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
