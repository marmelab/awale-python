from .board import newBoard, render, canPlay

def start():
    print("\n######### GAME STARTED ############\n")


    board = newBoard(12)
    print(render(board))

    currentPlayer = 1 #Constants ?

    position = AskPosition(board, currentPlayer)
    if position < 0:
        print("Invalid position")

    play(currentPlayer, position)
    currentPlayer = switchPlayer(currentPlayer)


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

def play(cPlayer, position):
    print("Player ({}) play {}.".format(cPlayer, position))


def switchPlayer(cPlayer):
    return cPlayer == 1 if 2 else 1