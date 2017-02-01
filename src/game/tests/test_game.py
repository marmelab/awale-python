import unittest
from ..game import get_complement_properties_player


class TestGame(unittest.TestCase):

    def test_get_complement_properties_player(self):
        player_one = get_complement_properties_player(0)
        player_two = get_complement_properties_player(1)

        self.assertEqual(player_one['min_position'], 0)
        self.assertEqual(player_two['min_position'], 6)
        self.assertEqual(player_one['max_position'], 6)
        self.assertEqual(player_two['max_position'], 12)
