import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestCardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.repo = PlayerRepository()

    def test_init(self):
        self.assertEqual(self.repo.players, [])
        self.assertEqual(self.repo.count, 0)

    def test_add(self):
        player = Advanced('Tony')
        self.repo.add(player)
        self.assertEqual(self.repo.players, [player])
        self.assertEqual(self.repo.count, 1)

    def test_add_already_exists(self):
        player = Advanced('Tony')
        self.repo.add(player)
        with self.assertRaises(ValueError) as ex:
            self.repo.add(player)
        self.assertEqual(str(ex.exception), "Player Tony already exists!")

    def test_remove(self):
        player = Advanced('Tony')
        self.repo.add(player)
        self.repo.remove('Tony')
        self.assertEqual(self.repo.players, [])
        self.assertEqual(self.repo.count, 0)

    def test_removing_empty_string_raises_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.repo.remove('')
        self.assertEqual(str(ex.exception), "Player cannot be an empty string!")

    def test_find(self):
        player = Advanced('Tony')
        self.repo.add(player)
        self.assertEqual(self.repo.find('Tony'), player)
