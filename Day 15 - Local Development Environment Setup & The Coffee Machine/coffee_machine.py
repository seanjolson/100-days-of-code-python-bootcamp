# Create coffee machine menu
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

# Create machine resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# Turn on the coffee machine
machine_power = True

while machine_power:
    # Prompt user for coffee selection
    menu_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the machine
    if menu_choice == "off":
        machine_power = False
    # Print machine report
    elif menu_choice == "report":
        print("Water: " + str(resources["water"]) + "ml")
        print("Milk: " + str(resources["milk"]) + "ml")
        print("Coffee: " + str(resources["coffee"]) + "g")
        print("Money: $" + str(resources["money"]))
    # Process drink request
    else:

        # Confirm there's enough resources for the selected drink
        enough_resources = True

        for ingredient in MENU[menu_choice]["ingredients"]:
            if MENU[menu_choice]["ingredients"][ingredient] > resources[ingredient]:
                print("Sorry, there is not enough " + ingredient + " for your " + menu_choice + ".")
                enough_resources = False

        # Process payment
        if enough_resources:
            print("Please insert coins.")

            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            # Confirm if the payment is sufficient
            payment_received = 0

            payment_received += quarters * 0.25
            payment_received += dimes * 0.10
            payment_received += nickels * 0.05
            payment_received += pennies * 0.01

            if payment_received < MENU[menu_choice]["cost"]:
                remaining_balance = MENU[menu_choice]["cost"] - payment_received
                
                print("Sorry, that's not enough money. You need $" + str(remaining_balance) + " more for your " + menu_choice + ". Money refunded.")
            else:
                if payment_received > MENU[menu_choice]["cost"]:
                    # Refund overpaid amount
                    overpaid_amount = payment_received - MENU[menu_choice]["cost"]
                    payment_received -= overpaid_amount
                    print("Here is $" + str(overpaid_amount) + " in change.")

                # Update resources
                resources["money"] += payment_received

                for ingredient in MENU[menu_choice]["ingredients"]:
                    resources[ingredient] -= MENU[menu_choice]["ingredients"][ingredient]

                # Make coffee
                print("Here is your " + menu_choice + ". Enjoy!")