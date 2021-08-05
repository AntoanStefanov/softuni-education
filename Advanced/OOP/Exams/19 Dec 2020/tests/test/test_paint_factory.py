import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.paint_factory = PaintFactory('Ime', 20)

    def test_init(self):
        self.assertEqual('Ime', self.paint_factory.name)
        self.assertEqual(20, self.paint_factory.capacity)
        self.assertEqual({}, self.paint_factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_add_ingredient_success(self):
        self.paint_factory.add_ingredient('white', 20)
        self.assertEqual({'white': 20}, self.paint_factory.ingredients)

    def test_add_ingredient_but_no_free_space(self):
        self.paint_factory.add_ingredient('white', 20)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 20)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_invalid_ingredient(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient('zileno', 20)
        self.assertEqual(f"Ingredient of type zileno not allowed in PaintFactory", str(ex.exception))

    def test_remove_non_existing_ingredient(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('white', 10)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_more_than_have(self):
        self.paint_factory.add_ingredient('white', 20)
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient('white', 200)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_success(self):
        self.paint_factory.add_ingredient('white', 20)
        self.paint_factory.remove_ingredient('white', 10)
        self.assertEqual({'white': 10}, self.paint_factory.ingredients)

    def test_property_products(self):
        self.assertEqual({}, self.paint_factory.products)


if __name__ == '__main__':
    unittest.main()
