import random
import win_loose


def play():
    user = input(
        "What's yout choice? (r) for rock, (p) for paper, (s) for scissors: "
    ).lower()
    computer = random.choice(["r", "p", "s"])
    if user == computer:
        return "Wooow it's a tie."
    elif win_loose.is_win(user, computer):
        return "Congratulations, you won."
    return "Sorry, you lost."


print(play())
