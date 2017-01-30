from .board import newBoard, render, canPlay

def start():
    print("\n######### GAME STARTED ############\n")


    board = newBoard(12)
    print(render(board))

    currentPlayer = 1 #Constants ?

    position = AskPosition(board, currentPlayer)
    print("Player ({}) play {}.".format(currentPlayer, position))


def AskPosition(board, cPlayer):

    try:
        position = int(input("Player ({0}), which position : ".format(cPlayer)))
    except ValueError:
        position =  -1

    while not canPlay(cPlayer, board, position):
        try:
            position = int(input("Wrong move, play again which position : "))
        except ValueError:
            position = -1

    return position