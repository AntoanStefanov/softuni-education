import unittest
from solution import Person


class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Tony', 'Stefanov', 20)

    def test_person_is_properly_initialised(self):
        self.assertEqual(self.person.first_name, 'Tony')
        self.assertEqual(self.person.second_name, 'Stefanov')
        self.assertEqual(self.person.age, 20)

    def test_person_full_name_combination_of_first_and_last_name(self):
        expected = 'Tony Stefanov'
        result = self.person.get_full_name()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
