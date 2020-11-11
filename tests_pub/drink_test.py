import unittest
from src_code_pub.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guiness", 3)

    
    def test_drink_has_name(self):
        self.assertEqual("Guiness", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(3, self.drink.price)
  
