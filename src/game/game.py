from .board import create_board, can_player_apply_position
from .renderer import render

def create_player(number):
        return {
            'number': number,
            'min_position': number * 6,
            'max_position': (1 + number) * 6,
            'min_pick': (1 - number) * 6,
            'max_pick': (2 - number) * 6,
        }

def start():
    print("\n######### GAME STARTED ############\n")

    board = create_board(12)  # Constants ?
    print(render(board))

    player = create_player(0)

    current_player = player

    position = ask_position(board, current_player)
    if position < 0:
        print("Invalid position")

    play_turn(board, current_player, position)
    switch_player(current_player)


def ask_position(board, current_player):

    try:
        position = int(input("Player ({0}), which position: "
                             .format(current_player['number'])))
    except ValueError:
        position = -1

    while not can_player_apply_position(current_player, board, position):
        try:
            position = int(input("Wrong move, play again which position: "))
        except ValueError:
            position = -1

    return position


def play_turn(board, current_player, position):
    print("Player ({}) play {}.".format(current_player['number'], position))
    end_position = deal_position(board, position)
    print(render(board))
    print(end_position)


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
