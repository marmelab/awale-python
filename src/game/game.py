from .board import create_board, can_player_apply_position, \
                   check_winner, winner
from .renderer import render
from .constants import CONST_PIT_COUNT


def start(player_one, player_two):
    print("\n######### GAME STARTED ############\n")

    board = create_board(CONST_PIT_COUNT)
    print(render(board))

    player_one = get_complement_properties_player(0, player_one)
    player_two = get_complement_properties_player(1, player_two)

    current_player = player_one

    while winner == -2:
        position = current_player['player'].get_position(board, current_player)
        if position < 0:
            print("Invalid position")
            continue

        play_turn(current_player, board, position)
        check_winner(current_player, board, position)
        switch_player(current_player)


def get_complement_properties_player(number, player=None):
    half_pit = int(CONST_PIT_COUNT / 2)
    return {
        'number': number,
        'min_position': number * half_pit,
        'max_position': (1 + number) * half_pit,
        'min_pick': (1 - number) * half_pit,
        'max_pick': (2 - number) * half_pit,
        'player': player,
    }


def play_turn(current_player, board, position):
    print("Player ({}) play {}.".format(current_player['number'], position))
    end_position = deal_position(board, position)
    print(render(board))


def deal_position(board, position):
    seeds = board[position]
    board[position] = 0
    i = position

    while seeds > 0:
        i += 1
        if i % 12 != position:
            board[i % 12] += 1
            seeds -= 1

    return i % 12


def switch_player(current_player):
    current_player['number'] = 0 if current_player['number'] == 1 else 1
