import unittest
from src_code_pub.customer import Customer
from src_code_pub.drink import Drink

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