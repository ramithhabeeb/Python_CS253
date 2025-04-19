"""
Task 1.2
    This program simulates a Rock-Paper-Scissors game between a human player and the computer.
    The rules of the game are:
    - Rock beats Scissors.
    - Scissors beats Paper.
    - Paper beats Rock.

    The program allows the user to:
    1. Input their choice (Rock, Paper, or Scissors).
    2. Play multiple rounds until they decide to quit by typing 'Quit'.
    3. View the choices of both the user and the computer for each round.
    4. See the total score (wins, losses, and ties) after each round.

    The program ensures:
    - Case-insensitive input handling.
    - Handling of invalid inputs with appropriate prompts.
    - Random choice generation for the computer using the random module.
"""

import random

def rps():
    choices = ['rock', 'paper', 'scissors']
    score = {'wins': 0, 'losses': 0, 'ties': 0}
    while 1:
        user_choice = input("Enter Rock, Paper, Scissors or Quit: ").strip().lower()
        if user_choice == 'quit':
            print("Game over.")
            break
        if user_choice not in choices:
            print("Invalid input. Try again.")
            continue
        comp_choice = random.choice(choices)
        print(f"You chose: {user_choice.capitalize()}, Computer chose: {comp_choice.capitalize()}")
        if user_choice == comp_choice:
            print("It's a tie!")
            score['ties'] += 1
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'scissors' and comp_choice == 'paper') or \
             (user_choice == 'paper' and comp_choice == 'rock'):
            print("You win!")
            score['wins'] += 1
        else:
            print("You lose!")
            score['losses'] += 1
        print(f"Score: Wins={score['wins']}, Losses={score['losses']}, Ties={score['ties']}\n")

rps()


