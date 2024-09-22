import unittest
from .context import src

class SquareTest(unittest.TestCase):
    def test_Square(self):
        self.assertEqual(src.Square(1), 1)
        self.assertTrue(src.Square(2) == 4)
        self.assertTrue(src.Square(3.0) == 9.0)
        
if __name__ == '__main__':
    unittest.main()