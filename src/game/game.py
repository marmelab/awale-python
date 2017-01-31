from .board import create_board, can_player_apply_position
from .renderer import render

def start():
    print("\n######### GAME STARTED ############\n")

    board = create_board(12) #Constants ?
    print(render(board))

    current_player = 1 #Constants ?

    position = ask_position(board, current_player)
    if position < 0:
        print("Invalid position")

    play_turn(board, current_player, position)
    current_player = switch_player(current_player)

def ask_position(board, current_player):

    try:
        position = int(input("Player ({0}), which position: ".format(current_player)))
    except ValueError:
        position =  -1

    while not can_player_apply_position(current_player, board, position):
        try:
            position = int(input("Wrong move, play again which position: "))
        except ValueError:
            position = -1

    return position

def play_turn(board, current_player, position):
    print("Player ({}) play {}.".format(current_player, position))
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
    return 2 if current_player == 1 else 1
