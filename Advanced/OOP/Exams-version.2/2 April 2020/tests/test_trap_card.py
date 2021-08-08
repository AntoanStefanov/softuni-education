import unittest

from project.card.trap_card import TrapCard


class TestMagicCard(unittest.TestCase):
    def setUp(self) -> None:
        self.card = TrapCard('card_name')

    def test_init(self):
        self.assertEqual(self.card.name, 'card_name')
        self.assertEqual(self.card.damage_points, 120)
        self.assertEqual(self.card.health_points, 5)

    def test_change_name_working(self):
        self.card.name = 'second_name'
        self.assertEqual(self.card.name, 'second_name')

    def test_change_name_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.name = ''
        self.assertEqual(str(ex.exception), "Card's name cannot be an empty string.")

    def test_change_damage_points_working(self):
        self.card.damage_points = 10
        self.assertEqual(self.card.damage_points, 10)

    def test_change_damage_points_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.damage_points = -1
        self.assertEqual(str(ex.exception), "Card's damage points cannot be less than zero.")

    def test_change_health_points_working(self):
        self.card.damage_points = 10
        self.assertEqual(self.card.damage_points, 10)

    def test_change_health_points_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.card.health_points = -1
        self.assertEqual(str(ex.exception), "Card's HP cannot be less than zero.")
