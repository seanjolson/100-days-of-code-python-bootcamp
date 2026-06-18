# Welcome players to the game
print('''
***************
   __________
  /\____;;___\`
 | /         /
 `. ())oo() .
  |\(%()*^^()^\`
 %| |-%-------|
% \ | %  ))   |
%  \|%________|
***************
      ''')
print("Weclome to Treasure Island.")
print("Your mission is to find the treasure.")

# Ask users which direction to go
cross_road = input("You're at a cross road. Where do you want to go?\n  Type 'left' or 'right'\n").lower()

# Ask users what to do at the lake
if cross_road == 'left':
    lake_island = input("You've come to a lake. There is an island in the middle of the lake.\n  Type 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    # Ask users which door to open
    if lake_island == 'wait':
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow, and one blue. Which color do you choose?\n").lower()

        # Decide whether users found the treasure
        if door_color == 'red':
            print("It's a room full of fire. Game Over.")
        elif door_color == 'yellow':
            print("You found the treasure! You win!")
        elif door_color == 'blue':
            print("You enter a room full of monsters. Game Over.")
    
    elif lake_island == 'swim':
        print("You get attached by an angry trout. Game Over.")

elif cross_road == 'right':
    print("You fell into a hole. Game Over.")