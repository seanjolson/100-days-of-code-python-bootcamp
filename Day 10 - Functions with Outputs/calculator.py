# Create calculator function
def calculator(first_number, second_number, selected_operation):
    # Calculate result
    if selected_operation == "+":
        result = first_number + second_number
    elif selected_operation == "-":
        result = first_number - second_number
    elif selected_operation == "*":
        result = first_number * second_number
    elif selected_operation == "/":
        result = first_number / second_number
    else:
        print("Invalid operation")

    return result

# Welcome users to calculator
print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')

# Prompt users for the first number
first_number = float(input("What's the first number?: "))

# Program loop
program_continue = True

while program_continue:
    # Prompt user to pick an operation
    operations = ["+", "-", "*", "/"]

    for operation in operations:
        print(operation)

    selected_operation = input("Pick an operation: ")

    # Prompt users for the second number
    second_number = float(input("What's the second number?: "))

    # Display result
    result = calculator(first_number, second_number, selected_operation)

    print(f"{first_number} {selected_operation} {second_number} = {result}")

    # Prompt user to continue or end the program
    continue_calculation = input(f"Type 'c' to continue calculating with {result}, type 'n' to start a new calculation, or type 'x' to stop calculating. ")

    # Execute user choice
    if continue_calculation == 'c':
        first_number = result
    elif continue_calculation == 'n':
        first_number = float(input("What's the first number?: "))
    elif continue_calculation == 'x':
        program_continue = False