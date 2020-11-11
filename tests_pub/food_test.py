import unittest
from src_code_pub.food import Food

class TestFood(unittest.TestCase):
  def setUp(self):
    self.food = Food("Chicken", 5, 3)
  
  def test_food_has_name(self):
    self.assertEqual("Chicken", self.food.name)

  def test_food_has_price(self):
    self.assertEqual(5, self.food.price)

  def test_food_has_rejuvenation_level(self):
    self.assertEqual(3, self.food.rejuvenation_level)

