

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


