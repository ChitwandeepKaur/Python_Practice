# Guessing Game

A simple Python number guessing game where the player has 3 attempts to guess a randomly generated number between 1 and 10.

## How to Play

1. Run the program with `python main.py`
2. You'll be prompted to guess a number between 1 and 10
3. You have **3 attempts** to guess the correct number
4. After each guess, you'll receive feedback:
   - **"Too Low!"** - Your guess is lower than the secret number
   - **"Too High!"** - Your guess is higher than the secret number
   - **"You guessed it!"** - You've found the correct number!
5. If you don't guess the number within 3 attempts, the game reveals the answer

## Game Features

- Random number generation using Python's `random` module
- User input validation (expects integers between 1-10)
- Feedback on each guess to guide your next attempt
- Limited attempts (3 guesses) to add challenge
- Automatic game end when the correct number is guessed

## Requirements

- Python 3.x
