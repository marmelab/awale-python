import sys
from .constants import CONST_PEBBLE_COUNT

# Take 2 if party is continue, -1 if equals or number of the player
winner = -2


def create_board(size):
    if size is None or size % 2 != 0:
        raise AttributeError("Board size size must be even.")

    # Create a new board, simple array
    return [CONST_PEBBLE_COUNT] * size


def can_player_apply_position(player, board, position):
    move_possible = (player['min_position'] <= position
                     < player['max_position'] and
                     board[position] != 0)

    if sum(board[player['min_pick']:player['max_pick']]) == 0:
        return move_possible  # todo add condition on starve and feed
    return move_possible


def check_winner(player, board, position):
    sys.exit(0)  # todo futur PR
