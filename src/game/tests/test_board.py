import unittest
from ..board import newBoard
from ..constants import CONST_PEBBLE_COUNT

class TestBoard(unittest.TestCase):

    def test_defaultNewBoard(self):
        self.assertEqual(newBoard(2), [CONST_PEBBLE_COUNT, CONST_PEBBLE_COUNT])
        self.assertEqual(newBoard(12), [CONST_PEBBLE_COUNT] * 12)

    def test_nullNewBord(self):
        with self.assertRaises(ValueError):
            newBoard(None)
        with self.assertRaises(ValueError):
            newBoard(13)
