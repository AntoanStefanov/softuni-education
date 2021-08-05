import unittest

from project.card.trap_card import TrapCard

DAMAGE_POINTS = 120
HEALTH_POINTS = 5


class TestTrapCard(unittest.TestCase):

    def test_empty_name_raises(self):
        with self.assertRaises(ValueError) as ex:
            TrapCard('')
        self.assertEqual("Card's name cannot be an empty string.", str(ex.exception))

    def test_name_setting(self):
        a = TrapCard('Magic_name')
        self.assertEqual('Magic_name', a.name)

    def test_health_setting(self):
        a = TrapCard('Magic_name')
        self.assertEqual(HEALTH_POINTS, a.health_points)
        self.assertEqual(DAMAGE_POINTS, a.damage_points)

    def test_health_raises_setting_below_zero(self):
        a = TrapCard('Tony')
        with self.assertRaises(ValueError) as ex:
            a.health_points = -1
        # ne checkva imeto na greshkata Ines
        self.assertEqual("Card's HP cannot be less than zero.", str(ex.exception))

    def test_damage_points_setting(self):
        a = TrapCard('Magic_name')
        self.assertEqual(HEALTH_POINTS, a.health_points)
        self.assertEqual(DAMAGE_POINTS, a.damage_points)

    def test_damage_points_raises_setting_below_zero(self):
        a = TrapCard('Tony')
        with self.assertRaises(ValueError) as ex:
            a.damage_points = -1
        # ne checkva imeto na greshkata Ines
        self.assertEqual("Card's damage points cannot be less than zero.", str(ex.exception))


if __name__ == '__main__':
    unittest.main()