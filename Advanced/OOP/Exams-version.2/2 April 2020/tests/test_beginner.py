import unittest

from project.card.card_repository import CardRepository
from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self) -> None:
        self.advanced_player = Beginner('Tony')

    def test_init(self):
        self.assertEqual(self.advanced_player.username, 'Tony')
        self.assertEqual(self.advanced_player.health, 50)
        self.assertTrue(isinstance(self.advanced_player.card_repository, CardRepository))

    def test_change_username_success(self):
        self.advanced_player.username = 'Roy'
        self.assertEqual(self.advanced_player.username, 'Roy')

    def test_change_username_expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced_player.username = ''
        self.assertEqual(str(ex.exception), "Player's username cannot be an empty string.")

    def test_change_health_success(self):
        self.advanced_player.health = 20
        self.assertEqual(self.advanced_player.health, 20)

    def test_change_health_expected_error(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced_player.health = -1
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_is_dead_true(self):
        self.advanced_player.health = 0
        self.assertTrue(self.advanced_player.is_dead)

    def test_is_dead_false(self):
        self.assertFalse(self.advanced_player.is_dead)

    def test_take_damage_success(self):
        self.advanced_player.take_damage(30)
        self.assertEqual(self.advanced_player.health, 20)

    def test_take_damage_raises_exception_for_negative_value(self):
        with self.assertRaises(ValueError) as ex:
            self.advanced_player.take_damage(-1)
        self.assertEqual(str(ex.exception), "Damage points cannot be less than zero.")
