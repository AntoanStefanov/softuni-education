from project.library import Library
import unittest


class TestLibrary(unittest.TestCase):
    def setUp(self) -> None:
        self.library = Library('ime')

