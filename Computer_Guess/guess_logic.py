import random
import min_max_for_list as mml


# Determines the guess range for computer guess.
def guess_func(lst, count, secret, guess, highest, lowest):
    maximum = mml.max_list(lst)
    minimum = mml.min_list(lst)
    if count <= 1:
        return random.randint(lowest, highest)
    elif guess > secret:
        return random.randint(minimum, guess)
    elif guess < secret:
        return random.randint(guess, maximum)
    else:
        return random.randint(minimum, maximum)
