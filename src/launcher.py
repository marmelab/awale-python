from game import game
from players import human_player

if __name__ == "__main__":
    try:
        game.start(human_player, human_player)
    except KeyboardInterrupt:
        print("\n\nBye bye, hope to see you again !\n\n")

    except Exception as e:
        print("An unexpected error occured, sorry.\nMessage: {0}\n"
              .format(str(e)))
