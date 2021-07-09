import unittest
import solution
from unittest import mock


class SolutionTests(unittest.TestCase):
    def test_get_my_daily_tasks(self):
        mock_value = {'userId': 1, 'id': 1,
                      'title': 'delectus aut autem', 'completed': False}
        with mock.patch('solution.get_tasks', return_value=mock_value):
            daily_tasks = solution.my_daily_to_do()
        self.assertEqual(daily_tasks, [{
                         'userId': 1,
                         'id': 1, 'title': 'delectus aut autem',
                         'completed': False,
                         }], 'Daily tasks didnt match, check the implementation')


if __name__ == '__main__':
    unittest.main()
