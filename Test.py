import unittest
import Lab1

class Test_TestAddSubtract(unittest.TestCase):
    def test_add(self):
        self.assertTrue(Lab1.Calculator.Add())

    def test_subtract(self):
        self.assertEqual(Lab1.Calculator.Subtract(),0)

    def test_multiply(self):
        self.assertTrue(Lab1.Calculator.Multiply())

if __name__ == '__main__':
    unittest.main()

