import unittest
from ..board import create_board
from ..constants import CONST_PEBBLE_COUNT


class TestBoard(unittest.TestCase):

    def test_defaultNewBoard(self):
        self.assertEqual(create_board(2),
                         [CONST_PEBBLE_COUNT, CONST_PEBBLE_COUNT])
        self.assertEqual(create_board(12), [CONST_PEBBLE_COUNT] * 12)

    def test_nullNewBord(self):
        with self.assertRaises(AttributeError):
            create_board(None)
        with self.assertRaises(AttributeError):
            create_board(13)
