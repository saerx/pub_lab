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

    def test_pub_can_sell_drink__over_18(self):
        customer_1 = Customer("Al McWhiggin", 40, 21)
        drink_1 = Drink("Guinness", 3, 2)
        self.pub.sell_drink(customer_1, drink_1)
        self.assertEqual(37, customer_1.wallet)
        self.assertEqual(203, self.pub.till)
        
    def test_pub_can_sell_drink__under_18(self):
        customer_2 = Customer("Andy", 500, 14)
        drink_1 = Drink("Guinness", 3, 2)
        self.pub.sell_drink(customer_2, drink_1)
        self.assertEqual(500, customer_2.wallet)
        self.assertEqual(200, self.pub.till)

    def test_make_customer_drunk(self):
        customer_1 = Customer("Al McWhiggin", 40, 21)
        drink_1 = Drink("Guinness", 3, 2)
        self.pub.sell_drink(customer_1, drink_1)
        self.assertEqual(2, customer_1.drunkenness)

    def test_knockback__true(self):
        customer_1 = Customer("Al McWhiggin", 40, 21)
        drink_2 = Drink("Death_Drink", 3, 11)
        self.pub.sell_drink(customer_1, drink_2)
        self.pub.sell_drink(customer_1, drink_2)
        self.assertEqual(37, customer_1.wallet)
        self.assertEqual(203, self.pub.till)
        self.assertEqual(11, customer_1.drunkenness)

