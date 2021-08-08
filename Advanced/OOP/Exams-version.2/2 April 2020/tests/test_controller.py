import unittest

from project.card.card_repository import CardRepository
from project.controller import Controller
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = Controller()

    def test_init(self):
        self.assertTrue(isinstance(self.controller.player_repository, PlayerRepository))
        self.assertTrue(isinstance(self.controller.card_repository, CardRepository))

    def test_add_player_beginner(self):
        msg = self.controller.add_player('Beginner', 'Tony')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(msg, "Successfully added player of type Beginner with username: Tony")

    def test_add_player_advanced(self):
        msg = self.controller.add_player('Advanced', 'Tony')
        self.assertEqual(self.controller.player_repository.count, 1)
        self.assertEqual(msg, "Successfully added player of type Advanced with username: Tony")

    def test_add_card_magic(self):
        msg = self.controller.add_card('Magic', 'Tony')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(msg, "Successfully added card of type MagicCard with name: Tony")

    def test_add_card_trap(self):
        msg = self.controller.add_card('Trap', 'Tony')
        self.assertEqual(self.controller.card_repository.count, 1)
        self.assertEqual(msg, "Successfully added card of type TrapCard with name: Tony")

    def test_add_player_card(self):  # cartata moje da sushtestuva veche ?
        self.controller.add_player('Advanced', 'Tony')
        self.controller.add_card('Magic', 'MagicCard')
        msg = self.controller.add_player_card('Tony', 'MagicCard')
        self.assertEqual(msg, "Successfully added card: MagicCard to user: Tony")

    def test_fight(self):
        self.controller.add_player('Beginner', 'Tony')
        self.controller.add_player('Beginner', 'Roy')
        msg = self.controller.fight('Tony', 'Roy')
        self.assertEqual(msg, "Attack user health 90 - Enemy user health 90")

    def test_report(self):
        self.controller.add_player('Beginner', 'Tony')
        self.controller.add_player('Beginner', 'Roy')
        msg = self.controller.report()
        self.assertEqual(msg, "Username: Tony - Health: 50 - Cards 0\nUsername: Roy - Health: 50 - Cards 0\n")

