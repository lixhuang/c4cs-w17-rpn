import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("2 0 -")
        self.assertEqual(2, result)
#    def test_exp(self):
#        result = rpn.calculate("2 0 ^")
#        self.assertEqual(1, result)

