import unittest
from ..board import create_board, can_player_apply_position
from ..game import get_complement_properties_player
from ..constants import CONST_PEBBLE_COUNT, CONST_PIT_COUNT


class TestBoard(unittest.TestCase):

    def test_default_new_board(self):
        self.assertEqual(
            create_board(2),
            [CONST_PEBBLE_COUNT, CONST_PEBBLE_COUNT]
        )
        self.assertEqual(
            create_board(CONST_PIT_COUNT),
            [CONST_PEBBLE_COUNT] * CONST_PIT_COUNT
        )

    def test_null_new_bord(self):
        with self.assertRaises(AttributeError):
            create_board(None)
        with self.assertRaises(AttributeError):
            create_board(13)

    def test_can_player_apply_position(self):
        player_one = get_complement_properties_player(0)
        player_two = get_complement_properties_player(1)
        board = create_board(CONST_PIT_COUNT)

        self.assertEqual(can_player_apply_position(player_one, board, 0), True)
        self.assertEqual(can_player_apply_position(player_two, board, 6), True)
        self.assertEqual(
            can_player_apply_position(player_one, board, 6),
            False
        )
        self.assertEqual(
            can_player_apply_position(player_two, board, 0),
            False
        )
        self.assertEqual(
            can_player_apply_position(player_one, board, 5),
            True
        )
        self.assertEqual(
            can_player_apply_position(player_two, board, 11),
            True
        )
        self.assertEqual(
            can_player_apply_position(player_one, board, 11),
            False
        )
        self.assertEqual(
            can_player_apply_position(player_two, board, 5),
            False
        )
