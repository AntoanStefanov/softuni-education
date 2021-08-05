import unittest

from project.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero('Joe', 10, 20, 30) # dmg = 300
        self.enemy = Hero('Joey', 10, 20, 30)# dmg = 300
    def test_init(self):
        self.assertEqual('Joe', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(30, self.hero.damage)

    def test_fight_yourself(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_fight_with_no_health(self): # ami iska li ako e na 0
        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_fight_with_enemy_no_health(self): # ami iska li ako e na 0
        self.enemy.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Joey. He needs to rest", str(ex.exception))

    def test_fight_draw(self):
        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_ally_win(self):
        self.hero.health = 1000
        self.assertEqual('You win', self.hero.battle(self.enemy))
        self.assertEqual(11, self.hero.level)
        self.assertEqual(705, self.hero.health)
        self.assertEqual(35, self.hero.damage)

    def test_enemy_win(self):
        self.enemy.health = 1000
        self.assertEqual('You lose', self.hero.battle(self.enemy))
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(705, self.enemy.health)
        self.assertEqual(35, self.enemy.damage)

    def test_str_method(self):
        self.assertEqual('Hero Joe: 10 lvl\nHealth: 20\nDamage: 30\n', str(self.hero))

