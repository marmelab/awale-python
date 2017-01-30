import unittest
from ..board import newBoard, isEven

class TestBoard(unittest.TestCase):

    def test_defaultNewBord(self):
        self.assertEqual(newBoard(12), [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])

    def test_nullNewBord(self):
        with self.assertRaises(ValueError):
            newBoard(None)
        with self.assertRaises(ValueError):
            newBoard(13)

    def test_isEven(self):
        self.assertEqual(isEven(1), False)
        self.assertEqual(isEven(2), True)