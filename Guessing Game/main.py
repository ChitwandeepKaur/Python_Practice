import random

number = random.randint(1, 10)
number_of_guesses = 0
while number_of_guesses < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    number_of_guesses += 1
    if guess < number:
        print("Too Low!")
    elif guess > number:
        print("Too High!")
    else:
        print("You guessed it!")
        break
else:
    print(f"Sorry, the number was {number}.")
