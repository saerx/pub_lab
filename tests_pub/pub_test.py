import unittest 
from src_code_pub.pub import Pub 

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Chicken Fun", 200)

    def test_pub_has_name(self):
        self.assertEqual("Chicken Fun", self.pub.name)
    
    def test_pub_has_till(self):
        self.assertEqual(200, self.pub.till)

