from art import logo
from random import randint

print(logo)
print("Hello! Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

attempts = input("Choose a difficulty. Type 'easy' or 'hard': ")

if attempts == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts to remaining to guess a number.")
else:
    attempts = 5
    print(f"You have {attempts} attempts to remaining to guess a number.")

for i in range(attempts):
    attempts -= 1

    user_answer = int(input("Make a guess: "))

    if user_answer == answer:
        print(f"You got it! The answer was {answer}")
        break
    elif user_answer > answer:
        print("Too high.")
    elif user_answer < answer:
        print("Too low.")

    if attempts == 0:
        print("You've run out the guesses. You lose!")
        break

    print("Guess again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
