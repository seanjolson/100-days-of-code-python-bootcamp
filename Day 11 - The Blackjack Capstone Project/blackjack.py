import random

# Ask user if they want to play blackjack
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

# Create card dictionary
cards = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

# Start game loop
while play_game == 'y':

    # Clear console
    print("\n" * 10)

    # Display ASCII art
    print('''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      '------'                           |__/           
    ''')

    # Deal cards
    player_cards = []
    dealer_cards = []

    def deal_card(person):
        if person == "player":
            player_cards.append(random.choice(list(cards)))
        elif person == "dealer":
            dealer_cards.append(random.choice(list(cards)))

    for i in range(2):
        deal_card("player")
        deal_card("dealer")

    # Display initial round
    print("Your cards: [" + player_cards[0] + ", " + player_cards[1] + "]")
    print("Dealer's first card: " + dealer_cards[0] + "\n")

    # Ask user if they want to get another card
    draw_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if draw_card == 'y':
        deal_card("player")

    # Display final hands
    if len(player_cards) == 3:
        print("\nYour final hand: [" + player_cards[0] + ", " + player_cards[1] + ", " + player_cards[2] + "]")
    else:
        print("\nYour final hand: [" + player_cards[0] + ", " + player_cards[1] + "]")

    print("Dealer's final hand: [" + dealer_cards[0] + ", " + dealer_cards[1] + "]")

    # Determine winner
    player_score = 0

    for card in player_cards:
        player_score += cards[card]

    dealer_score = 0

    for card in dealer_cards:
        dealer_score += cards[card]

    if player_score > 21:
        print("\nYou lose!")
    elif player_score > dealer_score:
        print("\nYou win!")
    elif dealer_score > player_score:
        print("\nYou lose!")

    # Prompt user to continue playing
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()