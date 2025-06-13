import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a calculator instance for all tests"""
        self.calc = SimpleCalculator()
    def test_addition(self):
        self.assertEqual(self.calc.add(10, 2),  12)
        self.assertEqual(self.calc.add(9, 3), 12)
        self.assertEqual(self.calc.add(1, 2),  3)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10, 2),  8)
        self.assertEqual(self.calc.subtract(9, 3), 6)
        self.assertEqual(self.calc.subtract(1, 2),  -1)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10, 2),  20)
        self.assertEqual(self.calc.multiply(9, 3), 27)
        self.assertEqual(self.calc.multiply(1, 2),  2)
    def test_division(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertIsNone(self.calc.divide(5, 0)) 
if __name__ == '__main__':
    unittest.main()