def is_win(word, guess):
    if ''.join(guess) == word:
        return f"You successfully guessed the word: {word}. You're safe ^-^."
    return f"Failed to guess the word: {word}. You've been hanged x_x."
