# Welcome user to the tip calculator
print("Welcome to the tip calculator!")

# Ask user for the total bill amount
total_bill = float(input("What was the total bill? $"))

# Ask user for the tip percent
tip_percent = int(input("How much of a tip would you like to give? 10%, 15%, 20%, or 25%? ")) * 0.01

# Ask user for how many people are splitting the bill
num_people = int(input("How many people are splitting the bill? "))

# Calculate how much each person should pay
price_per_person = "{:.2f}".format((total_bill + (total_bill * tip_percent)) / num_people)

# Print how much each person should pay
print("Each person should pay $" + str(price_per_person))