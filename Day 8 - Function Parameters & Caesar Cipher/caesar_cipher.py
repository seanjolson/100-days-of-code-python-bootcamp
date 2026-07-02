# Welcome users to program
print("Welcome to Caesar Cipher.")

program = True

# Define alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_index(character, list):
    return list.index(character)

def encode_message(message, shift):
    encoded_message = ""
    
    for letter in message:
        alphabet_index = get_index(letter, alphabet)
        shift_alphabet_index = alphabet_index + shift

        if shift_alphabet_index > 26:
            shift_alphabet_index -= 26

        encoded_message += alphabet[shift_alphabet_index]
    
    print(encoded_message)

def decode_message(message, shift):
    decoded_message = ""

    for letter in message:
        alphabet_index = get_index(letter, alphabet)
        shift_alphabet_index = alphabet_index - shift

        if shift_alphabet_index < 0:
            shift_alphabet_index += 26

        decoded_message += alphabet[shift_alphabet_index]
    
    print(decoded_message)

# Begin program loop
while program == True:
    
    # Prompt user to select mode
    mode = input("\nType 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    
    # Encode message
    if mode == "encode":
        message = input("\nType your message with no spaces:\n").lower()
        shift = int(input("\nType the shift number:\n"))

        encode_message(message, shift)

        # Ask user if they want to run again
        run_again = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    # Decode message
    elif mode == "decode":
        message = input("\nType your message with no spaces:\n").lower()
        shift = int(input("\nType the shift number:\n"))
        
        decode_message(message, shift)

        # Ask user if they want to run again
        run_again = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    
    # Handle error
    else: 
        print("\nPlease type a valid response.")
    
    if run_again == "no":
        program = False