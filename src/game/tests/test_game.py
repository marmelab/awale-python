import unittest
from ..game import switch_player, get_complement_properties_player

class TestGame(unittest.TestCase):

    def test_switch_player(self):

        player = get_complement_properties_player(0)
        switch_player(player)
        self.assertEqual(player['number'], 1)

        player = get_complement_properties_player(1)
        switch_player(player)
        self.assertEqual(player['number'], 0)
