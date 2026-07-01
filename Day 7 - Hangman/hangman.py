# Import random
import random

# Create possible list of words
word_list = ["makeup", "trade", "aid", "chart", "general", "terms", "indulge", "vegetation", "force", "report", "tenant", "steward", "village", "share", "convenience", "secretary", "present", "continuous", "loop", "speed", "bullet", "restoration", "develop", "braid", "storm", "tire", "equinox", "trap", "return", "alarm"]

# Welcome users to game
print('''
                                                   
  /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
 / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
/ __  / (_| | | | | (_| | | | | | | (_| | | | |
\/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/                       
      ''')

# Pick random word to guess
word_choice = random.choice(word_list)

list_word_choice = []

word_guess = []

for i in range(len(word_choice)):
    list_word_choice.append(word_choice[i])
    word_guess.append("_")

# Create starting lives count
lives_left = 6

# Game loop
while lives_left > 0:
    
    # Convert list to string
    str_word_guess = ""

    for char in word_guess:
        str_word_guess += char

    # Display progress to user
    print("Word to guess: " + str_word_guess)
    
    # Prompt user to guess a letter
    letter_guess = input("Guess a letter: ").lower()

    # Check if guessed letter is in word
    found_letter = False
    
    if letter_guess in list_word_choice:
        found_letter = True
        
        # Find all instance of letter
        letter_indices = [i for i, letter in enumerate(list_word_choice) if letter == letter_guess]
        
        for index in letter_indices:
            word_guess[index] = letter_guess
    
    # Display guess results to user
    if found_letter == False:
        print("You guessed " + letter_guess + ". That's not in the word, you lose a life!")
        lives_left -= 1
    
    if lives_left == 6:
        game_board = '''
                       +---+
                       |   |
                           |
                           |
                           |
                           |
                     =========
                     '''
    elif lives_left == 5:
        game_board = '''
                       +---+
                       |   |
                       0   |
                           |
                           |
                           |
                     =========
                     '''
    elif lives_left == 4:
        game_board = '''
                       +---+
                       |   |
                       0   |
                       |   |
                           |
                           |
                     =========
                     '''
    elif lives_left == 3:
        game_board = '''
                       +---+
                       |   |
                       0   |
                      /|   |
                           |
                           |
                     =========
                     '''
    elif lives_left == 2:
        game_board = '''
                       +---+
                       |   |
                       0   |
                      /|\  |
                           |
                           |
                     =========
                     '''
    elif lives_left == 1:
        game_board = '''
                       +---+
                       |   |
                       0   |
                      /|\  |
                      /    |
                           |
                     =========
                     '''
    elif lives_left == 0:
        game_board = '''
                       +---+
                       |   |
                       0   |
                      /|\  |
                      / \  |
                           |
                     =========
                     '''

    print(game_board)
    print("********************" + str(lives_left) + "/6 lives left********************")

    # End game 
    if lives_left == 0:
        print(game_board)
        print("You lost all your lives! The word was " + word_choice + ". Game over!")
    elif "_" not in word_guess:
        print(game_board)
        print("The word was " + word_choice + ". You win!")
        lives_left = 0