import unittest
from extended_list import IntegerList


class IntegerListTests(unittest.TestCase):
    # Do not forget to test the constructor ?????????????????
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, 4)

    def test_init_method(self):
        self.assertEqual(self.int_list.get_data(), [1, 2, 3, 4])

    def test_add_method_adding_element_and_returns_the_list(self):
        actual_list = self.int_list.add(5)
        expected_list = [1, 2, 3, 4, 5]
        self.assertEqual(actual_list, expected_list)

    def test_add_method_adding_element_that_is_not_int(self):
        with self.assertRaises(ValueError):
            self.int_list.add(5.2)

    def test_remove_index_method_and_returns_the_element(self):
        actual_element = self.int_list.remove_index(0)
        expected_element = 1
        self.assertEqual(actual_element, expected_element)

    def test_remove_index__method_out_of_range(self):
        with self.assertRaises(IndexError):
            self.int_list.remove_index(4)

    def test_init_takes_only_ints(self):
        list = IntegerList(4.2, 3, 'baba')
        self.assertEqual(list.get_data(), [3])

    def test_get_method_if_it_returns_the_element_on_specific_index(self):
        actual_element = self.int_list.get(0)
        expected_element = 1
        self.assertEqual(actual_element, expected_element)

    def test_get_method_if_throws_error_if_out_of_index(self):
        with self.assertRaises(IndexError):
            self.int_list.get(4)

    def test_insert_method(self):
        self.int_list.insert(0, 100)
        self.assertEqual(self.int_list.get_data(), [100, 1, 2, 3, 4])

    def test_insert_method_if_throws_error_if_our_of_range(self):
        with self.assertRaises(IndexError):
            self.int_list.insert(4, 2)

    def test_insert_method_if_throws_error_if_element_not_int(self):
        with self.assertRaises(ValueError):
            self.int_list.insert(0, 1.2)

    def test_if_get_biggest_method_returns_biggest_number(self):
        actual_element = self.int_list.get_biggest()
        expected_element = 4
        self.assertEqual(actual_element, expected_element)

    def test_if_get_index_method_returns_the_index_of_given_el(self):
        actual_index = self.int_list.get_index(1)
        expected_index = 0
        self.assertEqual(actual_index, expected_index)


if __name__ == '__main__':
    unittest.main()
