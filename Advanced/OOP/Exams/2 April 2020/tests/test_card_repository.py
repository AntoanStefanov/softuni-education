import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard


class TestCardRepository(unittest.TestCase):
    def test_init(self):
        card_repo = CardRepository()
        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

    def test_add_card(self):
        card_repo = CardRepository()
        card = MagicCard('Tony')

        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

        card_repo.add(card)

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

    def test_add_if_we_add_same_card_error_expected(self):
        card_repo = CardRepository()

        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

        card = MagicCard('Tony')
        card_repo.add(card)

        self.assertEqual(1, card_repo.count)
        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))  # ines way, same as above maybe?

        with self.assertRaises(ValueError) as ex:
            card_repo.add(card)
        self.assertEqual(f"Card {card.name} already exists!", str(ex.exception))

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

    def test_remove_card(self):
        card_repo = CardRepository()
        card = MagicCard('Tony')

        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

        card_repo.add(card)

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

        card_repo.remove('Tony')

        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))
        self.assertEqual(0, card_repo.count)

    def test_removing_empty_string_raises_exception(self):
        card_repo = CardRepository()
        card = MagicCard('Tony')

        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

        card_repo.add(card)

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

        with self.assertRaises(ValueError) as ex:
            card_repo.remove('')
        self.assertEqual("Card cannot be an empty string!", str(ex.exception))

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

    def test_find_method(self):
        card_repo = CardRepository()
        card = MagicCard('Tony')

        self.assertEqual(0, card_repo.count)
        self.assertEqual([], card_repo.cards)
        self.assertEqual(0, len(card_repo.cards))  # ines way, same as above maybe?

        card_repo.add(card)

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)

        res = card_repo.find('Tony')
        self.assertEqual(card, res)

        self.assertEqual([card], card_repo.cards)
        self.assertEqual(1, len(card_repo.cards))
        self.assertEqual(1, card_repo.count)


if __name__ == '__main__':
    unittest.main()
