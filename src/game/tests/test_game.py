import unittest
from ..game import switch_player, create_player

class TestGame(unittest.TestCase):


    def test_switchPlayer(self):

        player = create_player(0)
        switch_player(player)
        self.assertEqual(player['number'], 1)

        player = create_player(1)
        switch_player(player)
        self.assertEqual(player['number'], 0)
