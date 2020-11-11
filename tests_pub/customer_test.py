import unittest
from src_code_pub.customer import Customer

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