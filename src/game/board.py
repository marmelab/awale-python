import sys
from .constants import PEBBLE_COUNT, PIT_COUNT

GAME_NO_WINNER = -1
GAME_CONTINUE = -2


def create_board(size):
    if size is None or size % 2 != 0:
        raise AttributeError("Board size size must be even.")

    # Create a new board, simple array
    return [PEBBLE_COUNT] * size


def can_player_apply_position(player, board, position):
    try:
        is_empty_pit = (board[position] == 0)
    except IndexError:
        return False

    is_player_can_move = (player['min_position'] <=
                          position <
                          player['max_position'])

    move_possible = is_player_can_move and not is_empty_pit

    if sum(board[player['min_pick']:player['max_pick']]) == 0:
        is_starving = will_starve_player(player, board, position, None)
        can_feed_player = can_feed(player, board, None)
        return move_possible and (not is_starving or not can_feed_player)
    return move_possible


def deal_position(board, position):
    seeds = board[position]
    board[position] = 0
    i = position

    while seeds > 0:
        i += 1
        if i % PIT_COUNT != position:
            board[i % PIT_COUNT] += 1
            seeds -= 1

    return i % PIT_COUNT


def pick(player, board, position, score):
    end_position = deal_position(board, position)

    def is_pick_possible(x):
        return (player['min_pick'] <= end_position < player['max_pick']
                and 2 <= board[end_position] <= 3)

    while is_pick_possible(end_position):
        score[player['number']] += board[end_position]
        board[end_position] = 0
        end_position -= 1

    return board, score


def will_starve_player(player, board, position, score=None):
    pick(player, board, position, score)
    min_pick = player['min_pick']
    max_pick = player['max_pick']
    starving = (sum(board[min_pick:max_pick]) == 0)
    return starving


def can_feed(player, board, score=None):
    min_position = player['min_position']
    max_position = player['max_position']
    cannot_feed = True

    for i in range(min_position, max_position):
        starving = will_starve_player(player, board, i, score)
        cannot_feed = cannot_feed and starving

    return not cannot_feed


def check_winner(player, board, position, game_state, score):
    if game_state == GAME_CONTINUE:
        min_pick = player['min_pick']
        max_pick = player['max_pick']
        number_player = player['number']
        starving = sum(board[min_pick:max_pick]) == 0

        min_score = int(((PEBBLE_COUNT * PIT_COUNT) / 2))

        if starving or score[number_player] >= min_score:
            game_state = number_player
        elif score[1 - number_player] >= min_score:
            game_state = 1 - number_player

        return score, game_state
