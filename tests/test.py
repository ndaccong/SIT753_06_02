import unittest
from .context import src

class SquareTest(unittest.TestCase):
    def test_square(self):
        self.assertEqual(src.square(1), 1)
        self.assertTrue(src.square(2) == 4)
        
if __name__ == '__main__':
    unittest.main()