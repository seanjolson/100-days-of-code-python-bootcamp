# Import random functionality
import random

# Display game start
print('''
▄█▀   ▄█ ▄▄ ▄█▀ ▄▄▀▄▄ ▄▄▀▄▄      ▀██▀ ▄▄ ▄▄ ▄█▀      ▄█▀█▄ ▄█ ▄▄ ▄█▀█▄▀█▄ ██▀▄  ▄█▀ ██▀▄▄
██    ██ ██ ██  ██    ██          ██  ██ ██ ██       ██ ██ ██ ██ ██ ██ ██ ██ ██ ██  ██ █▀
██▀█▄ ██ ██ ██▀  ▀▀▄▄  ▀▀▄▄       ██  ██▀██ ██▀      ██ ██ ██ ██ ██ ██ ██ ██▀█▄ ██▀ ██▀█▄
██ ██ ██ ██ ██  ▄▄ ██ ▄▄ ██       ██  ██ ██ ██       ██ ██ ██ ██ ██ ██ ██ ██ ██ ██  ██ ██
▀█▄██ ▀▀▄▀▀ ▀█▄ ▀▀▄▀▀ ▀▀▄▀▀       ██  ██ ██ ▀█▄      ██ ██ ▀▀▄▀▀ ██ ▀▀ ██ ██▄▀▀ ▀█▄ ██ ██
''')
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.\n")

# Calculate random number
random_number = random.randint(1, 100)

# Display answer - for testing purposes only
print("Pssst, the correct answer is " + str(random_number) + ".")

# Ask user to choose difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
print('\n')

# Determine attempts
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

# Start game loop
while attempts > 0:

    # Display remaining attempts
    print("You have " + str(attempts) + " attempts remaining to guess the number.")

    # Get user guess
    guess = int(input("Make a guess: "))

    # Determine if guess matches the random number
    if guess > random_number:
        attempts -= 1

        print("Too high.")

        if attempts == 0:
            print("You ran out of attempts. The correct number was " + str(random_number) + ".")
        else:
            print("Guess again.\n")
    elif guess < random_number:
        attempts -= 1

        print("Too low.")

        if attempts == 0:
            print("You ran out of attempts. The correct number was " + str(random_number) + ".")
        else:
            print("Guess again.\n")
    else:
        print("You got it! The answer was " + str(random_number) + ".")

        attempts = 0