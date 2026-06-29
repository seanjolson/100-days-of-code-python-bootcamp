# Import random
import random

# Welcome users to program
print("Welcome to the PyPassword Generator!")

# Ask users for password parameters
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# List of possible characters
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
           "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols = ["!", "$", "*", "+", "-", "@", "#", "%", "&", "(", ")"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Generate list of randomly selected characters
rand_characters = []

for i in range(num_letters):
    rand_characters.append(random.choice(letters))
for i in range(num_symbols):
    rand_characters.append(random.choice(symbols))
for i in range(num_numbers):
    rand_characters.append(random.choice(numbers))

# Assemble password with randomly selected characters
password = ""

for i in range(len(rand_characters)):
    
    # Save a randomly selected character from choice list
    rand_character = random.choice(rand_characters)

    # Add randomly selected character to password
    password += rand_character

    # Remove randomly selected character from choice list
    rand_characters.remove(rand_character)

# Output password
print(password)