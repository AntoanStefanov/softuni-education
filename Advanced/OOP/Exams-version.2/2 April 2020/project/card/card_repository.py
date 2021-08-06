class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card):
        if card in self.cards:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card: str):
        if card == '':
            raise ValueError("Card cannot be an empty string!")
        c = self.find(card)
        if c:
            self.cards.remove(c)
            self.count -= 1

    def find(self, name):
        for card in self.cards:
            if card.name == name:
                return card
