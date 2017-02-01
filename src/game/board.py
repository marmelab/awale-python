import sys
from .constants import CONST_PEBBLE_COUNT, CONST_PIT_COUNT

GAME_NO_WINNER = -1
GAME_CONTINUE = -2

game_state = GAME_CONTINUE


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


def deal_position(board, position):
    seeds = board[position]
    board[position] = 0
    i = position

    while seeds > 0:
        i += 1
        if i % CONST_PIT_COUNT != position:
            board[i % CONST_PIT_COUNT] += 1
            seeds -= 1

    return i % CONST_PIT_COUNT


def pick(player, board, position):
    score = [0] * 2
    end_position = deal_position(board, position)

    def is_pick_possible(x):
        return (player['min_pick'] <= end_position < player['max_pick']
                and 2 <= board[end_position] <= 3)

    while is_pick_possible(end_position):
        score[player['number']] += board[end_position]
        board[end_position] = 0
        end_position -= 1

    return board, score


def check_winner(player, board, position):
    sys.exit(0)  # todo futur PR
