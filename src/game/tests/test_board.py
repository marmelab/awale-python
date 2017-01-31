import unittest
from ..board import newBoard, isEven, displayRow
from ..constants import CONST_PEBBLE_COUNT

class TestBoard(unittest.TestCase):

    def test_defaultNewBord(self):
        self.assertEqual(newBoard(2), [CONST_PEBBLE_COUNT, CONST_PEBBLE_COUNT])
        self.assertEqual(newBoard(12), [CONST_PEBBLE_COUNT] * 12)

    def test_nullNewBord(self):
        with self.assertRaises(ValueError):
            newBoard(None)
        with self.assertRaises(ValueError):
            newBoard(13)

    def test_isEven(self):
        self.assertEqual(isEven(1), False)
        self.assertEqual(isEven(2), True)

    def test_displayRow(self):
        board = newBoard(12)
        self.assertEqual(displayRow(board), '1(4) 2(4) 3(4) 4(4) 5(4) 6(4) 7(4) 8(4) 9(4) 10(4) 11(4) 12(4) ')

        board = newBoard(6)
        self.assertEqual(displayRow(board, 1), '2(4) 3(4) 4(4) 5(4) 6(4) 7(4) ')
