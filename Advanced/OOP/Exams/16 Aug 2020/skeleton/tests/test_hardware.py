import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('SSD', 'Power', 100, 200)

    # nomer 1
    def test_attributes_are_set(self):
        self.assertEqual('SSD', self.hardware.name)
        self.assertEqual('Power', self.hardware.type)
        self.assertEqual(100, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    # Tuk se broqt dva testa v judge edin da raise exception,
    # drugiq da proveri kakvo suobshtenie vrushta raise-natiq exception
    # nomer 2 i nomer 4
    def test_unsuccessful_installation(self):
        software = Software('Software', 'Type', 200, 300)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    # nomer 3 test judje
    def test_successful_uninstall(self):
        software = Software('Software', 'Type', 50, 100)
        # И това бачка
        # self.hardware.install(software)
        self.hardware.software_components.append(software)
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == '__main__':
    unittest.main()
