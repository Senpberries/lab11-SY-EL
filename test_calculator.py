# https://github.com/Senpberries/lab11-SY-EL
# Partner 1: Sen Yang
# Partner 2: Evelyn Lopez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 5), 4)
        self.assertEqual(add(0, 0), 0)


    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(3, 7), -4)
        self.assertEqual(subtract(-5, -5), 0)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 2), 6)
        self.assertEqual(mul(-3, 6), -18)
        self.assertEqual(mul(-4, -1), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(3, 12), 4)
        self.assertEqual(div(-3, 27), -9)
        self.assertEqual(div(-48, 0), 0)
    # ##########################

    ####### Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 12)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(10, 100), 2)
        self.assertEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(64), 8)
        with self.assertRaises(ValueError):
            square_root(-4)
        with self.assertRaises(ValueError):
            square_root(-6)


# Do not touch this
if __name__ == "__main__":
    unittest.main()