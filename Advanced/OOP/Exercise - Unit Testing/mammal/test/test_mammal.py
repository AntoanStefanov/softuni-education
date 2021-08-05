import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal('Joji', 'Lion', 'Roar')

    def test_init(self):
        self.assertEqual('Joji', self.mammal.name)
        self.assertEqual('Lion', self.mammal.type)
        self.assertEqual('Roar', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_sound(self):
        self.assertEqual("Joji makes Roar", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Joji is of type Lion", self.mammal.info())

if __name__ == '__main__':
    unittest.main()