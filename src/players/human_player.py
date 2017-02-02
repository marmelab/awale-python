from game.board import can_player_apply_position
from game.exitException import ExitException


def get_position(board, current_player):
    try:
        position = int(input("Player ({}), which position: "
                             .format(current_player['number'] + 1)))
    except KeyboardInterrupt as e:
        raise ExitException(e)
    except ValueError:
        position = -1

    while not can_player_apply_position(current_player, board, position):
        try:
            position = int(
                input("Wrong move, play again which position: ")
            )
        except ValueError:
            position = -1

    return position
