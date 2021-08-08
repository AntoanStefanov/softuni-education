import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self) -> None:
        self.attacker = Beginner('Tony')
        self.enemy = Advanced('Roy')
        self.magic_card = MagicCard('magic_card')

    def test_start_fight_with_dead(self):
        self.attacker.health = 0
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(str(ex.exception), 'Player is dead!')

    def test_fight_no_winner(self):
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 90)
        self.assertEqual(self.enemy.health, 250)

    def test_fight_attacker_winner(self):
        self.magic_card.damage_points = 220
        self.attacker.card_repository.add(self.magic_card)
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(self.enemy.health, 0)

    def test_fight_raises_exception_if_attack_more_than_health(self):
        self.magic_card.damage_points = 220
        self.enemy.card_repository.add(self.magic_card)
        with self.assertRaises(ValueError) as ex:
            BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(str(ex.exception), "Player's health bonus cannot be less than zero.")

    def test_fight_enemy_winner(self):
        self.magic_card.damage_points = 90
        self.enemy.card_repository.add(self.magic_card)
        BattleField.fight(self.attacker, self.enemy)
        self.assertEqual(self.attacker.health, 0)
