from .constants import CONST_PEBBLE_COUNT

def newBoard(size):
    if size is None or size % 2 != 0:
        raise ValueError("Board size size must be even.")

    # Create a new board, simple array
    return [CONST_PEBBLE_COUNT] * size

def canPlay(player, board, position):
    return True
