import unittest
from ..board import create_board
from ..renderer import display_row


class TestRenderer(unittest.TestCase):

    def test_display_row(self):
        board = create_board(12)

        self.assertEqual(display_row(board), ' '.join([
            '0(4) 1(4) 2(4) 3(4) 4(4) 5(4)',
            '6(4) 7(4) 8(4) 9(4) 10(4) 11(4) ',
        ]))

        board = create_board(6)

        self.assertEqual(display_row(board, 1), ' '.join([
            '1(4) 2(4) 3(4)',
            '4(4) 5(4) 6(4) ',
        ]))
