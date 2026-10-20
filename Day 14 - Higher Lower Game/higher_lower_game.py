# Import random module
import random

# Create logo and vs art
logo = '''
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                         
                                                                         
░▒▓█▓▒░      ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓█████████████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
'''

# Create game data
data = [
    {
        "name": "Mantine",
        "pokedex number": 226,
        "base stat total": 485,
        "type": "Water/Flying"
    },
    {
        "name": "Torchic",
        "pokedex number": 255,
        "base stat total": 310,
        "type": "Fire"
    },
    {
        "name": "Shroodle",
        "pokedex number": 944,
        "base stat total": 290,
        "type": "Poison/Normal"
    },
    {
        "name": "Mabosstiff",
        "pokedex number": 943,
        "base stat total": 505,
        "type": "Dark"
    },
    {
        "name": "Tangrowth",
        "pokedex number": 465,
        "base stat total": 535,
        "type": "Grass"
    },
    {
        "name": "Grimmsnarl",
        "pokedex number": 861,
        "base stat total": 510,
        "type": "Dark/Fairy"
    }   
]

# Initiate game loop
play_game = True

# Randomly select a pokemon to start
def random_pokemon():
    random_pokemon = random.choice(data)

    data.remove(random_pokemon)

    return random_pokemon

# Create function to format text
def print_pokemon(pokemon):
    pokemon_string = pokemon["name"] + " (#" + str(pokemon["pokedex number"]) + "), a " + pokemon["type"] + " type."
    
    return pokemon_string

# Initiate score counter
score = 0

# Generate first pokemon
pokemon_a = random_pokemon()

print(logo)

# Play game
while play_game:
    print("\n")

    # Generate choices
    pokemon_b = random_pokemon()

    # Print
    print("Compare A: " + print_pokemon(pokemon_a) + "\n")
    print("VS. \n")
    print("Against B: " + print_pokemon(pokemon_b) + "\n")

    # Prompt user to select
    selection = input("Who has the higher base stat total? Type 'a' or 'b': ").lower()

    # Determine correct selection
    if pokemon_a["base stat total"] > pokemon_b["base stat total"]:
        answer = "a"
    else:
        answer = "b"

    # Validate user selection
    if selection == answer:
        score += 1
        print("You're right! Current score: " + str(score) + ".")

        pokemon_a = pokemon_b
    else:
        print("Sorry, that's wrong. Final score: " + str(score) + ".")

        play_again = input("Type 'y' to play again or 'n' to stop playing. ").lower()

        if play_again == 'n':
            play_game = False

        score = 0