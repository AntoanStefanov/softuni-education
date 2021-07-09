import unittest
from worker import Worker


class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.worker = Worker('Tony', 10000, 100)

    def test_initializing_worker_correctly(self):
        self.assertEqual(self.worker.name, 'Tony')
        self.assertEqual(self.worker.salary, 10000)
        self.assertEqual(self.worker.energy, 100)

    def test_energy_incrementation_after_rest_method(self):
        expected_energy = 101
        self.worker.rest()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_money_increasing_correctly_after_work_method(self):
        expected_money = 10000
        self.worker.work()
        self.assertEqual(self.worker.money, expected_money)

    def test_error_if_the_worker_tries_to_work_with_negative_or_equal_to_zero_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception):
            self.worker.work()

    def test_energy_decremenation_after_work_method(self):
        expected_energy = 99
        self.worker.work()
        self.assertEqual(self.worker.energy, expected_energy)

    def test_get_info_method_correct_return(self):
        result = self.worker.get_info()
        excepted_result = 'Tony has saved 0 money.'
        self.assertEqual(result, excepted_result)


if __name__ == '__main__':
    unittest.main()
