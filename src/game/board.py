import sys
from .constants import CONST_PEBBLE_COUNT

GAME_NO_WINNER = -1
GAME_CONTINUE = -2

winner = GAME_CONTINUE


def create_board(size):
    if size is None or size % 2 != 0:
        raise AttributeError("Board size size must be even.")

    # Create a new board, simple array
    return [CONST_PEBBLE_COUNT] * size


def can_player_apply_position(player, board, position):
    is_empty_pit = (board[position] == 0)
    is_player_can_move = (player['min_position'] <=
                          position <
                          player['max_position'])

    move_possible = is_player_can_move and not is_empty_pit

    if sum(board[player['min_pick']:player['max_pick']]) == 0:
        return move_possible  # todo add condition on starve and feed
    return move_possible


def check_winner(player, board, position):
    sys.exit(0)  # todo futur PR
