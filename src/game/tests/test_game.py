import unittest
from ..game import switchPlayer, askPosition


class TestGame(unittest.TestCase):

    def test_switchPlayer(self):
        self.assertEqual(switchPlayer(1), 2)
        self.assertEqual(switchPlayer(2), 1)

