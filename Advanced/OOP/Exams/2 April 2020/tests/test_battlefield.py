import unittest

from project.battle_field import BattleField
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def test_fight_raises_exception_if_attacker_is_dead(self):
        attacker = Advanced('Tony')
        enemy = Advanced('Zoy')

        attacker.health = 0

        with self.assertRaises(ValueError) as ex:
            BattleField.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_fight_raises_exception_if_enemy_is_dead(self):
        attacker = Advanced('Tony')
        enemy = Advanced('Zoy')

        enemy.health = 0

        with self.assertRaises(ValueError) as ex:
            BattleField.fight(attacker, enemy)
        self.assertEqual("Player is dead!", str(ex.exception))

    def test_beginners_health_is_increased(self):
        pass

    def test_health_bonus_for_each_card_add_card_health_points(self):
        attacker = Advanced('Tony')
        enemy = Advanced('Zoy')
        trap_card = TrapCard('Trap')

        attacker.card_repository.add(trap_card)
        enemy.card_repository.add(trap_card)

        self.assertEqual(250, attacker.health)
        self.assertEqual(250, enemy.health)

        BattleField.fight(attacker, enemy)

        self.assertEqual(135, attacker.health)
        self.assertEqual(135, enemy.health)

        self.assertFalse(attacker.is_dead)
        self.assertFalse(enemy.is_dead)

    def test_enemy_health_goes_below_zero_raises_exception(self):
        attacker = Advanced('Tony')
        enemy = Beginner('Zoy')
        trap_card = TrapCard('Trap')
        trap_card_2 = TrapCard('Trap2')

        attacker.card_repository.add(trap_card)
        attacker.card_repository.add(trap_card_2)
        enemy.card_repository.add(trap_card)

        self.assertEqual(250, attacker.health)
        self.assertEqual(50, enemy.health)

        with self.assertRaises(ValueError) as ex:
            BattleField.fight(attacker, enemy)
        self.assertEqual("Player's health bonus cannot be less than zero.", str(ex.exception))
        self.assertEqual(260, attacker.health)
        self.assertFalse(attacker.is_dead)
        self.assertFalse(enemy.is_dead)

    def test_enemy_dies_in_fight(self):
        attacker = Advanced('Tony')
        enemy = Beginner('Zoy')
        trap_card = TrapCard('Trap')
        trap_card_2 = TrapCard('Trap2')

        attacker.card_repository.add(trap_card)
        attacker.card_repository.add(trap_card_2)
        enemy.card_repository.add(trap_card)

        self.assertEqual(250, attacker.health)
        self.assertEqual(50, enemy.health)
        enemy.health += 175
        BattleField.fight(attacker, enemy)
        self.assertEqual(260, attacker.health)
        self.assertEqual(0, enemy.health)
        self.assertFalse(attacker.is_dead)
        self.assertTrue(enemy.is_dead)


if __name__ == '__main__':
    unittest.main()
