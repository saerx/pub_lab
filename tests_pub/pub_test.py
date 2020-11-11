import unittest 
from src_code_pub.pub import Pub 
from src_code_pub.customer import Customer
from src_code_pub.drink import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Chicken Fun", 200)

    def test_pub_has_name(self):
        self.assertEqual("Chicken Fun", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(200, self.pub.till)

    def test_pub_can_sell_drink(self):
        customer_1 = Customer("Al McWhiggin", 40)
        drink_1 = Drink("Guiness", 3)
        self.pub.sell_drink(customer_1, drink_1)
        self.assertEqual(37, customer_1.wallet)
        self.assertEqual(203, self.pub.till)

