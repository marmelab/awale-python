import unittest
from ..board import newBoard
from ..renderer import displayRow

class TestRenderer(unittest.TestCase):

    def test_displayRow(self):
        board = newBoard(12)
        self.assertEqual(displayRow(board), '1(4) 2(4) 3(4) 4(4) 5(4) 6(4) 7(4) 8(4) 9(4) 10(4) 11(4) 12(4) ')

        board = newBoard(6)
        self.assertEqual(displayRow(board, 1), '2(4) 3(4) 4(4) 5(4) 6(4) 7(4) ')
