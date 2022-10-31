from player import HumanPlayer, GeniusComputerPlayer
from game import TicTacToe
import time
import random


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = random.choice(["X", "O"])
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            letter = "O" if letter == "X" else "X"

        time.sleep(1.0)

    if print_game:
        print("It's a tie")


if __name__ == "__main__":
    # x_player = HumanPlayer("X")
    x_player = HumanPlayer("X")
    o_player = GeniusComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
