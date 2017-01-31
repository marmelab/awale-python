import unittest
from ..game import switch_player

class TestGame(unittest.TestCase):

    def test_switchPlayer(self):
        self.assertEqual(switch_player(1), 2)
        self.assertEqual(switch_player(2), 1)
