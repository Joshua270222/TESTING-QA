# test_calculation.py
import unittest
from calculation import add, subtract

class TestCalculation(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 1), 2)
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(10, 3), 7)

    def test_add_invalid_input(self):
        with self.assertRaises(TypeError):
            add(1, '2')
            add('1', 2)

if __name__ == '__main__':
    unittest.main()
