import json
import string
from win_loose import is_win as wl
from word import valid_word as vw

# Opens and parses json file
with open("E:/Téléchargements/words.json") as word_list:
    data = word_list.read()
words = json.loads(data)


def main():
    secret_word = vw(words)
    secret_letters = set(secret_word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    count = len(secret_letters)

    while len(secret_letters) > 0 and count > 0:
        if len(used_letters) > 0:
            sorted_used_letters = ' '.join(sorted(used_letters))
            print(f"""You have {count} chances left.
You have already used these letters: {sorted_used_letters}""")

        word_list = [
            letter if letter in used_letters else '_' for letter in secret_word
        ]
        print("Current word: ", " ".join(word_list))

        guess = input("Guess a letter: ").upper()
        print("")

        if guess in alphabet - used_letters:
            used_letters.add(guess)
            if guess in secret_letters:
                secret_letters.remove(guess)
            else:
                count -= 1

        elif guess in used_letters:
            print("You have already use that letter. Please try again")

        else:
            print("Invalid character. Please try again.")

        word_list2 = [
            letter if letter in used_letters else '_' for letter in secret_word
        ]

    check = wl(secret_word, word_list2)
    print(check)


if __name__ == "__main__":
    main()
