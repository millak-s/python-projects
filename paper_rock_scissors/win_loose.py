def is_win(player, opponent):
    if ((player == "r" and opponent == "s")
            or (player == "s" and opponent == "p")
            or (player == "p" and opponent == "r")):
        return True
