import random
from guess_logic import guess_func


def computer_guess(target):
    secret = int(target)
    count = 0
    guess = 0
    memory = []
    print(f"Guess a number between 1 and {secret}")

    while count < 5:
        # Determines the guess range for computer guess.
        guess = guess_func(memory, guess, secret)
        if guess in memory:
            pass
        elif guess == secret:
            print(f"Well done! You've guessed the number {secret} correctly.")
            break
        elif guess < secret:
            print(f"Ooops!! {guess} is too low, try again.")
            memory.append(guess)
            count += 1
        else:
            print(f"Ooops!! {guess} is too high, try again.")
            memory.append(guess)
            count += 1
    print("Game Over!")

secret = input("Type the secret number: ")
computer_guess(secret)
