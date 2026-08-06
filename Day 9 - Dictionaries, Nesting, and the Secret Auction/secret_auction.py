# Print ASCII art
print('''
       ___________
       \         /
        )_______(
        |"""""""|_.-._,.---------.,_.-._
        |       | | |               | | ''-.
        |       |_| |_             _| |_..-'
        |_______| '-' `'---------'` '-'
        )"""""""(
       /_________|
       `'-------'`
     .-------------.
    /_______________|
      ''')

# Set up container for bids
bids = {}

# Create function to determine silent auction winner
def determine_winner():
    highest_bid = ["Bid Start", 0]

    for key, value in bids.items():
        if value > highest_bid[1]:
            highest_bid = [key, value]

    return highest_bid

# Set up program loop
active_bidding = True

while active_bidding:
    # Prompt user for their name
    user_name = input("What is your name?:  ")

    # Prompt user for their bid
    user_bid = int(input("What is your bid?:  $"))

    # Add bid to dictionary
    bids[user_name] = user_bid

    # Prompt user for if there's any additional bidders
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()

    # Add space to conceal previous bids
    print('\n' * 20)

    # Stop program if there's no more bids
    if more_bids == 'no':
        highest_bid = determine_winner()
        print(highest_bid[0] + " won the auction with a bid of $" + str(highest_bid[1]) + ".")
        active_bidding = False