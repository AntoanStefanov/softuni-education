import unittest

from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hardware = Hardware('R', 'Type', 100, 100)

    def test_init(self):
        self.assertEqual(self.hardware.name, 'R')
        self.assertEqual(self.hardware.type, 'Type')
        self.assertEqual(self.hardware.capacity, 100)
        self.assertEqual(self.hardware.memory, 100)

    def test_install_success(self):
        software = Software('Name', 'Type', 100, 100)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)

    def test_install_unsuccess(self):
        software = Software('Name', 'Type', 101, 101)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual(str(ex.exception), 'Software cannot be installed')
        self.assertEqual(len(self.hardware.software_components), 0)

    def test_uninstall_success(self):
        software = Software('Name', 'Type', 100, 100)
        self.hardware.install(software)
        self.assertEqual(len(self.hardware.software_components), 1)
        self.hardware.uninstall(software)
        self.assertEqual(len(self.hardware.software_components), 0)

####### PODOBRI ZADACHATA SI VE LOILIO CQLATAAA POVECHE PORPERTRY I METHODI ####
