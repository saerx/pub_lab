import unittest
from src_code_pub.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Al McWhiggin", 40)

    def test_customer_has_name(self):
        self.assertEqual("Al McWhiggin", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(40, self.customer.wallet)