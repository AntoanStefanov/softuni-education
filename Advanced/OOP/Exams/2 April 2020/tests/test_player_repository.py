import unittest

from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestPlayerRepository(unittest.TestCase):
    def test_init(self):
        player_repo = PlayerRepository()
        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players)) # ines way, same as above maybe?

    def test_add_player(self):
        player_repo = PlayerRepository()
        player = Advanced('Tony')

        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players)) # ines way, same as above maybe?

        player_repo.add(player)

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

    def test_add_if_we_add_same_player_error_expected(self):
        player_repo = PlayerRepository()

        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players)) # ines way, same as above maybe?

        player = Advanced('Tony')
        player_repo.add(player)

        self.assertEqual(1, player_repo.count)
        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players)) # ines way, same as above maybe?

        with self.assertRaises(ValueError) as ex:
            player_repo.add(player)
        self.assertEqual(f"Player {player.username} already exists!", str(ex.exception))

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

    def test_remove_player(self):
        player_repo = PlayerRepository()
        player = Advanced('Tony')

        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players))  # ines way, same as above maybe?

        player_repo.add(player)

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

        player_repo.remove('Tony')

        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players))
        self.assertEqual(0, player_repo.count)

    def test_removing_empty_string_raises_exception(self):
        player_repo = PlayerRepository()
        player = Advanced('Tony')

        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players))  # ines way, same as above maybe?

        player_repo.add(player)

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

        with self.assertRaises(ValueError) as ex:
            player_repo.remove('')
        self.assertEqual("Player cannot be an empty string!", str(ex.exception))

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

    def test_find_method(self):
        player_repo = PlayerRepository()
        player = Advanced('Tony')

        self.assertEqual(0, player_repo.count)
        self.assertEqual([], player_repo.players)
        self.assertEqual(0, len(player_repo.players))  # ines way, same as above maybe?

        player_repo.add(player)

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)

        res = player_repo.find('Tony')
        self.assertEqual(player, res)

        self.assertEqual([player], player_repo.players)
        self.assertEqual(1, len(player_repo.players))
        self.assertEqual(1, player_repo.count)


if __name__ == '__main__':
    unittest.main()