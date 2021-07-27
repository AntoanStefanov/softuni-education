import unittest

from car_manager import Car


class CarManagerTests(unittest.TestCase):
    def setUp(self):
        self.car_manager = Car('plastic', 'G-turbo', 2, 80)

    def test_init(self):
        self.assertEqual('plastic', self.car_manager.make)
        self.assertEqual('G-turbo', self.car_manager.model)
        self.assertEqual(2, self.car_manager.fuel_consumption)
        self.assertEqual(80, self.car_manager.fuel_capacity)

    def test_make_property(self):
        self.assertEqual('plastic', self.car_manager.make)

    def test_make_setter(self):
        self.car_manager.make = 'metal'
        self.assertEqual('metal', self.car_manager.make)

    def test_make_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_property(self):
        self.assertEqual('G-turbo', self.car_manager.model)

    def test_model_setter(self):
        self.car_manager.model = 'GAZ'
        self.assertEqual('GAZ', self.car_manager.model)

    def test_model_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_property(self):
        self.assertEqual(2, self.car_manager.fuel_consumption)

    def test_fuel_consumption_setter(self):
        self.car_manager.fuel_consumption = 10
        self.assertEqual(10, self.car_manager.fuel_consumption)

    def test_fuel_consumption_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_property(self):
        self.assertEqual(80, self.car_manager.fuel_capacity)

    def test_fuel_capacity_setter(self):
        self.car_manager.fuel_capacity = 10
        self.assertEqual(10, self.car_manager.fuel_capacity)

    def test_fuel_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_below_or_equal_to_zero(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_fuel_more_than_capacity(self):
        self.car_manager.refuel(90)
        self.assertEqual(80, self.car_manager.fuel_amount)

    def test_refuel_with_fuel_more_less_capacity(self):
        self.car_manager.refuel(10)
        self.assertEqual(10, self.car_manager.fuel_amount)

    def test_drive_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            self.car_manager.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_successful(self):
        self.car_manager.fuel_amount = 50
        self.car_manager.drive(1)
        self.assertEqual(49.98, self.car_manager.fuel_amount)


if __name__ == '__main__':
    unittest.main()
