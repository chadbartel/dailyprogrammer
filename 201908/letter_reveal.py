"""
Weekly # 26 - Mini Challenges
../r/dailyprogrammer/comments/56mfgz/weekly_26_mini_challenges/

Description: It's 'hangman'.
Input: alpha character
Example:
    >_____
    >L (Input)
    >__LL_
    >H (Input)
    >H_LL_
    >E (Input)
    >HELL_
    >O (Input)
    >HELLO
Extra Challenge: Give the user a limited number of guesses.
Challenge by: u/Blocks_

Author: Chad Bartel
Date:   8/6/2019
"""

from random import randint

SECRET_WORDS = [
    'HELLO',
    'WORLD',
    'PYTHON',
    'DAILY',
    'PROGRAMMING',
    'OCCURRENCES',
    'THICK',
    'CREAMY'
]


def letter_reveal(secret_word: str = None, hard_mode: bool = False):

    # Select a word to guess at random.
    if not secret_word:
        i = randint(0, len(SECRET_WORDS)-1)
        answer = list(SECRET_WORDS[i])
        answer_copy = list(SECRET_WORDS[i])
    else:
        answer = list(secret_word.strip().upper())
        answer_copy = list(secret_word.strip().upper())
    guess = list("_" * len(answer))

    # Check if hard mode is enabled.
    if hard_mode:
        print(f"Wow! Hard mode, huh?\n"
              f"You have {len(guess)} attempts to guess the word!\n"
              f"Good luck!\n")

    # Alert user game is starting and reveal word length with "_".
    print("Game is starting! Your word is below...")
    print(" ".join(guess))

    # Begin gameplay loop.
    i = 0
    while i < len(answer):

        # Prompt user for input.
        user_input = input("Guess a letter: ").upper()

        if not user_input.isalpha() or len(user_input) != 1:
            # Validate user input is a single alpha character.
            print("Bad input! Try entering a single character from A-Z!")
        else:
            # If user input is in answer, reveal letter(s).
            if user_input in answer:
                letter_indices = [
                    i for i, x in enumerate(answer) if x == user_input
                ]
                print(f"{user_input} appears in the answer "
                      f"{len(letter_indices)} time(s)!")
                for li in letter_indices:
                    # Increment counter for each letter and remove from answer.
                    i += 1
                    guess[li] = user_input
                    answer[li] = "_"
            # User input is not in answer.
            else:
                i += 1
                print(f"{user_input} does not appear in the answer...")

        print(" ".join(guess))

    if guess == answer_copy:
        print("Congratulations! You guessed the word!\nThanks for playing!")
    else:
        print("Whoops! Looks like you didn't figure it out! "
              "Try again next time!")
        print("ANSWER:\t", " ".join(answer_copy))

    return None


if __name__ == "__main__":
    letter_reveal()
