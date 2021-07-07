import unittest
from cat import Cat


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('Tomy')

    # def test_initilizing(self):
    #     pass
    # SHOULD WE TEST INIT ?
    def test_is_size_increased_after_eating(self):
        self.cat.eat()
        expected_size = 1
        actual_size = self.cat.size
        self.assertEqual(expected_size, actual_size)

    def test_if_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_raise_error_if_cat_is_already_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_raise_error_if_cat_is_not_fed_and_try_to_sleep(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_if_cat_is_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
