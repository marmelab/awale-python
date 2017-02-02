import unittest
from ..board import create_board
from ..renderer import display_board_top, display_board_bottom


class TestRenderer(unittest.TestCase):

    def test_display_board_top(self):
        board = create_board(6)
        half = int(len(board) / 2)

        self.assertEqual(display_board_top(board, half), ' '.join([
            '\t5 [4]\t4 [4]\t3 [4]',
        ]))

    def test_display_board_bottom(self):
        board = create_board(6)
        half = int(len(board) / 2)

        self.assertEqual(display_board_bottom(board, half), ' '.join([
            '\t0 [4]\t1 [4]\t2 [4]',
        ]))
