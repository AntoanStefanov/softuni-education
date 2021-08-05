import unittest

from project.controller import Controller

class TestController(unittest.TestCase):
    def test_init_controller(self):
        c = Controller()
        self.assertEqual(0, len(c.player_repository.players))
        self.assertEqual(0, len(c.card_repository.cards))

    def test_add_players_success(self):
        c = Controller()
        res1 = c.add_player('Beginner', 'beginner_username')
        res2 = c.add_player('Advanced', 'advanced_username')
        self.assertEqual(2, len(c.player_repository.players))
        self.assertEqual(f"Successfully added player of type Beginner with username: beginner_username", res1)
        self.assertEqual(f"Successfully added player of type Advanced with username: advanced_username", res2)

    def test_add_cards_success(self):
        c = Controller()
        res1 = c.add_card('Magic', 'magic_card_name')
        res2 = c.add_card('Trap', 'trap_card_name')
        self.assertEqual(2, len(c.card_repository.cards))
        self.assertEqual(f"Successfully added card of type MagicCard with name: magic_card_name", res1)
        self.assertEqual(f"Successfully added card of type TrapCard with name: trap_card_name", res2)

    def test_add_player_card(self):
        c = Controller()
        c.add_player('Beginner', 'beginner_username')
        c.add_card('Magic', 'magic_card_name')

        res = c.add_player_card('beginner_username', 'magic_card_name')
        self.assertEqual("Successfully added card: magic_card_name to user: beginner_username", res)

    def test_fight(self):
        c = Controller()
        c.add_player('Beginner', 'beginner_username')
        c.add_player('Advanced', 'advanced_username')
        res = c.fight('beginner_username', 'advanced_username')
        self.assertEqual("Attack user health 90 - Enemy user health 250", res)

    def test_report(self):
        c = Controller()
        c.add_player('Beginner', 'beginner_username')
        c.add_player('Advanced', 'advanced_username')
        actual = c.report()
        expected = 'Username: beginner_username - Health: 50 - Cards 0\nUsername: advanced_username - Health: 250 - Cards 0\n'
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
