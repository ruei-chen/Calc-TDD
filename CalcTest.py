import unittest
from Calc import Calculator  # The class we are going to implement


class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5
        
    def test_sub(self):
        calc = Calculator()
        result = calc.sub(5, 3)
        self.assertEqual(result, 2)
        
    def test_mul(self):
        calc = Calculator()
        result = calc.mul(5, 3)
        self.assertEqual(result, 15)
        
    def test_div(self):
        calc = Calculator()
        self.assertEqual(calc.div(10, 2), 5.0)
        
    def test_div_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.div(10, 0)


if __name__ == "__main__":
    unittest.main()
    