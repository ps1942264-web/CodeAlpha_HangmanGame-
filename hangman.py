"""
Task 1: Hangman Game
--------------------
A simple text-based Hangman game played in the console.

Rules:
  * The computer picks a random word from a list of 5 words.
  * The player guesses one letter at a time.
  * The player is allowed a maximum of 6 incorrect guesses.

Concepts used: random, while loop, if-else, strings, lists.
"""

import random

# ----------------------------------------------------------------------
# Game settings
# ----------------------------------------------------------------------
WORDS = ["python", "program", "keyboard", "developer", "computer"]
MAX_WRONG = 6

# ASCII art for each stage (index = number of wrong guesses made so far)
HANGMAN_STAGES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
]


def get_display_word(secret_word, guessed_letters):
    """Return the word with unguessed letters hidden, e.g. 'p y _ _ o _'."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_game():
    """Play one full round of Hangman."""
    secret_word = random.choice(WORDS)  # pick a random word
    guessed_letters = []                # every letter the player has tried
    wrong_guesses = 0                   # number of incorrect guesses so far

    print("\n==============================")
    print("      WELCOME TO HANGMAN!")
    print("==============================")
    print(f"I'm thinking of a {len(secret_word)}-letter word.")
    print(f"You can make up to {MAX_WRONG} incorrect guesses.")

    while wrong_guesses < MAX_WRONG:
        # --- Show the current state of the game ---
        print(HANGMAN_STAGES[wrong_guesses])
        display = get_display_word(secret_word, guessed_letters)
        print("\nWord:", display)
        print("Guessed letters:", " ".join(sorted(guessed_letters)) or "none yet")
        print(f"Wrong guesses left: {MAX_WRONG - wrong_guesses}")

        # --- Check for a win ---
        if "_" not in display:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word.upper()}")
            return

        # --- Get and validate the player's guess ---
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter (a-z).")
        elif guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
        else:
            guessed_letters.append(guess)
            if guess in secret_word:
                print(f"✅ Good job! '{guess}' is in the word.")
            else:
                wrong_guesses += 1
                print(f"❌ Sorry, '{guess}' is not in the word.")

    # --- Loop ended: the player ran out of guesses ---
    print(HANGMAN_STAGES[MAX_WRONG])
    print(f"\n💀 Game over! The word was: {secret_word.upper()}")


def main():
    """Run the game and offer to play again."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing Hangman. Goodbye!")
            break


if __name__ == "__main__":
    main()
