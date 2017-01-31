from .constants import CONST_PEBBLE_COUNT


def create_board(size):
    if size is None or size % 2 != 0:
        raise AttributeError("Board size size must be even.")

    # Create a new board, simple array
    return [CONST_PEBBLE_COUNT] * size


def can_player_apply_position(player, board, position):

    if sum(board[player['min_pick']:player['max_pick']]) == 0:
        print('oui')
    else:
        print('non')
        return (player['min_position'] <= position < player['max_position'] and
                board[position] != 0)
