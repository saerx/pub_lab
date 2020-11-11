import unittest
from src_code_pub.customer import Customer
from src_code_pub.drink import Drink
from src_code_pub.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Al McWhiggin", 40, 21)

    def test_customer_has_name(self):
        self.assertEqual("Al McWhiggin", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(40, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(21, self.customer.age)

    def test_customer_drunkenness_level(self):
        self.assertEqual(0, self.customer.drunkenness)

    def test_increase_drunkenness(self):
        drink_1 = Drink("Guinness", 3, 2)
        self.customer.increase_drunkenness(drink_1)
        self.assertEqual(2, self.customer.drunkenness)

    def test_decrease_drunkenness(self):
        drink_1 = Drink("Guinness", 3, 2)
        food_1 = Food("Chicken", 5, 3)
        self.customer.increase_drunkenness(drink_1)
        self.customer.increase_drunkenness(drink_1)
        self.customer.decrease_drunkenness(food_1)
        self.assertEqual(1, self.customer.drunkenness)




        