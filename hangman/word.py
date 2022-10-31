import random


def valid_word(lst):
    word = random.choice(lst["data"])
    while "-" in word or " " in word:
        word = random.choice(lst)
    return word.upper()
