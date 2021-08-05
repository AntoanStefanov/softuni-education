import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10, 15)

    def test_init(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(15, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_success(self):
        self.vehicle.drive(2)
        self.assertEqual(7.5, self.vehicle.fuel)

    def test_drive_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10)
        self.assertEqual('Not enough fuel', str(ex.exception))

    def test_refuel_successful(self):
        self.vehicle.refuel(0)
        self.assertEqual(10, self.vehicle.fuel)

    def test_refuel_unsuccessful(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual('Too much fuel', str(ex.exception))

    def test_str(self):
        self.assertEqual('The vehicle has 15 horse power with 10 fuel left and 1.25 fuel consumption', str(self.vehicle))
