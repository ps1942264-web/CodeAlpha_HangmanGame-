# Hangman Game 🎮

A simple text-based Hangman game written in Python. Guess the secret word one letter at a time before you run out of attempts!

## Features
- Random word chosen from a list of 5 predefined words
- Maximum of 6 incorrect guesses
- ASCII-art hangman that updates after every wrong guess
- Input validation (single letters only, no repeated guesses)
- Option to play again

## Concepts Used
`random` module · `while` loop · `if-else` · strings · lists

## How to Run
1. Install [Python 3](https://www.python.org/downloads/)
2. Clone this repository or download `hangman.py`
3. Run in a terminal:
   ```bash
   python hangman.py
   ```

## How to Play
- The word is shown as underscores, e.g. `_ _ _ _ _ _`
- Type one letter and press Enter
- Correct letters are revealed; wrong letters add a part to the hangman
- Win by revealing the whole word, lose if the hangman is completed (6 wrong guesses)

## Sample Output
```
Word: p _ _ _ o _
Guessed letters: o p s
Wrong guesses left: 5

Guess a letter:
```
