import unittest

from project.pet_shop import PetShop


class TestsPetShop(unittest.TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop('Ime')

    def test_init(self):
        self.assertEqual(self.pet_shop.name, 'Ime')
        self.assertEqual(self.pet_shop.food, {})
        self.assertEqual(self.pet_shop.pets, [])

    def test_add_food_error(self):
        with self.assertRaises(ValueError) as ex:
            self.pet_shop.add_food('food', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_not_existing_food(self):
        res = self.pet_shop.add_food('food', 1)
        self.assertEqual(res, f"Successfully added {1:.2f} grams of food.")
        self.assertEqual(self.pet_shop.food, {'food': 1})

    def test_add_existing_food(self):
        self.pet_shop.add_food('food', 1)
        self.pet_shop.add_food('food', 1)
        self.assertEqual(self.pet_shop.food, {'food': 2})

    def test_add_pet(self):
        res = self.pet_shop.add_pet('name')
        self.assertEqual(res, "Successfully added name.")

    def test_add_same_pet(self):
        self.pet_shop.add_pet('name')
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet('name')
        self.assertEqual('Cannot add a pet with the same name', str(ex.exception))

    def test_feed_not_existing_pet(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet('food', 'name')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_pet_with_not_existing_food(self):
        self.pet_shop.add_pet('name')
        res = self.pet_shop.feed_pet('food', 'name')
        self.assertEqual('You do not have food', res)

    def test_feed_pet_if_food_lower_than_100(self):
        self.pet_shop.add_food('food', 1)
        self.pet_shop.add_pet('name')
        res = self.pet_shop.feed_pet('food', 'name')
        self.assertEqual(res, 'Adding food...')
        self.assertEqual(self.pet_shop.food['food'], 1001)

    def test_feed_pet_succeeds(self):
        self.pet_shop.add_food('food', 200)
        self.pet_shop.add_pet('name')
        res = self.pet_shop.feed_pet('food', 'name')
        self.assertEqual("name was successfully fed", res)
        self.assertEqual(self.pet_shop.food['food'], 100)

    def test_repr(self):

        self.assertEqual(f'Shop Ime:\nPets: ', repr(self.pet_shop))
