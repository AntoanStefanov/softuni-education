import unittest

from project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room('name', 100, 2)

    def test_init(self):
        self.assertEqual(self.room.family_name, 'name')
        self.assertEqual(self.room.budget, 100)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(self.room.children, [])
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_assignment_successful(self):
        self.room.expenses = 1
        self.assertEqual(self.room.expenses, 1)

    def test_expenses_assignment_unsuccessful(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual(str(ex.exception), 'Expenses cannot be negative')


if __name__ == '__main__':
    unittest.main()
