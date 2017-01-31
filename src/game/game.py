from .board import newBoard, render, canPlay

def start():
    print("\n######### GAME STARTED ############\n")


    board = newBoard(12) #Constants ?
    print(render(board))

    currentPlayer = 1 #Constants ?

    position = askPosition(board, currentPlayer)
    if position < 0:
        print("Invalid position")

    play(board, currentPlayer, position)
    currentPlayer = switchPlayer(currentPlayer)


def askPosition(board, cPlayer):

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

def play(board, cPlayer, position):
    print("Player ({}) play {}.".format(cPlayer, position))
    endPosition = dealPosition(board, position)
    print(render(board))
    print(endPosition)

def dealPosition(board, position):
    seeds = board[position]
    board[position] = 0
    i = position

    while seeds > 0:
        i += 1
        if i % 12 != position:
            board[i % 12] += 1
            seeds -= 1

    return i % 12

def switchPlayer(cPlayer):
    return 2 if cPlayer == 1 else 1
