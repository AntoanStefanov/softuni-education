import unittest

from project.player.advanced import Advanced

INITIAL_HEALTH = 250


class TestAdvanced(unittest.TestCase):
    def test_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            Advanced('')
        self.assertEqual("Player's username cannot be an empty string.", str(ex.exception))

    def test_name_setting(self):
        a = Advanced('Tony')
        self.assertEqual('Tony', a.username)

    def test_health_setting(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)

    def test_health_raises_setting_below_zero(self):
        a = Advanced('Tony')
        with self.assertRaises(ValueError) as ex:
            a.health = -1
        # ne checkva imeto na greshkata Ines
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))

    def test_is_dead(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)
        self.assertFalse(a.is_dead)
        a.health = 0
        self.assertEqual(0, a.health)
        self.assertTrue(a.is_dead)

    def test_take_damage_raises_exception_for_negative_value(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)
        with self.assertRaises(ValueError) as ex:
            a.take_damage(-50)
        self.assertEqual("Damage points cannot be less than zero.", str(ex.exception))
        self.assertEqual(INITIAL_HEALTH, a.health)

    def test_take_damage(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)
        a.take_damage(50)
        self.assertEqual(200, a.health)

    def test_take_zero_damage(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)
        a.take_damage(0)
        self.assertEqual(INITIAL_HEALTH, a.health)

    def test_take_damage_player_will_be_dead(self):
        a = Advanced('Tony')
        self.assertEqual(INITIAL_HEALTH, a.health)
        with self.assertRaises(ValueError) as ex:
            a.take_damage(260)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))


if __name__ == "__main__":
    unittest.main()
