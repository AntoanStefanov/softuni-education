import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = CardRepository()

    def test_init(self):
        self.assertEqual(self.repo.cards, [])
        self.assertEqual(self.repo.count, 0)

    def test_add(self):
        card = MagicCard('card_name')
        self.repo.add(card)
        self.assertEqual(self.repo.cards, [card])
        self.assertEqual(self.repo.count, 1)

    def test_add_already_exists(self):
        card = MagicCard('card_name')
        self.repo.add(card)
        with self.assertRaises(ValueError) as ex:
            self.repo.add(card)
        self.assertEqual(str(ex.exception), "Card card_name already exists!")

    def test_remove(self):
        card = MagicCard('card_name')
        self.repo.add(card)
        self.repo.remove('card_name')
        self.assertEqual(self.repo.cards, [])
        self.assertEqual(self.repo.count, 0)

    def test_removing_empty_string_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.remove('')
        self.assertEqual(str(ex.exception), "Card cannot be an empty string!")

    def test_find(self):
        card = MagicCard('card_name')
        self.repo.add(card)
        self.assertEqual(self.repo.find('card_name'), card)
