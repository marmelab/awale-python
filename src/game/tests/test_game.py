import unittest
from ..game import switchPlayer, askPosition


class TestGame(unittest.TestCase):

    def test_switchPlayer(self):
        self.assertEqual(switchPlayer(1), 2)
        self.assertEqual(switchPlayer(2), 1)

    #def test_askPosition(self):
        #board = newBoard(12)

        #self.assertEqual(askPosition(board, 1))
        #self.assertEqual(askPosition(board, 2))

