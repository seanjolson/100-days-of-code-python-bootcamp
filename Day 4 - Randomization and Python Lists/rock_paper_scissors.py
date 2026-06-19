# Import random functionality
import random

# Welcome users to the game
print("Welcome to Rock, Paper, Scissors!")

# Ask user for their choice
user_choice = input("What do you choose? Type 'Rock', 'Paper', or 'Scissors'.\n").lower()

# Generate computer choice
options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)

# Determine winner
if user_choice == "rock":
    if computer_choice == "rock":
        print('''
        You chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        It's a draw!
            ''')
    elif computer_choice == "paper":
        print('''
        You chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        The computer wins!
            ''')
    elif computer_choice == "scissors":
        print('''
        You chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        You win!
            ''')
elif user_choice == "paper":
    if computer_choice == "rock":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        Computer chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        You win!
            ''')
    elif computer_choice == "paper":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        It's a draw!
            ''')
    elif computer_choice == "scissors":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        You lose!
            ''')
elif user_choice == "scissors":
    if computer_choice == "rock":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)__
                (_____)
                (_____)
                (____)
        ---.__(___)
            
        You lose!
            ''')
    elif computer_choice == "paper":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                    _______)
                    _______)
        ---.__________)
            
        You win!
            ''')
    elif computer_choice == "scissors":
        print('''
        You chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        Computer chose:
            _______
        ---'   ____)______
                    ______)
                __________)
              (____)
        ---.__(___)
            
        It's a draw!
            ''')
