import unittest

from project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room('name', 100, 2)

    def test_init(self):
        self.assertEqual('name', self.room.family_name)
        self.assertEqual(100, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        self.assertEqual(0, self.room.expenses) # purvi test

    def test_expenses_assignment_successful(self):
        self.room.expenses = 10
        self.assertEqual(10, self.room.expenses)

    def test_expenses_assignment_unsuccessful(self):
        with self.assertRaises(ValueError) as ex:
            self.room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(ex.exception))


if __name__ == '__main__':
    unittest.main()
