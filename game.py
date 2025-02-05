'''Adventure Text Game
Author: Damian Ugalde
Version: 1.0
Description: 
This is a text-based game where the player navigates a world
by making decisions.'''

# Below is the welcome message and introduction.
print("Welcome to the Adventure Game!")
print("Your journey begins here...")

# Ask for the Player's name.
player_name = input('What is your name, oh great Adventurer? ')
# Concatenate Strings to create a personalized message.
#print('Welcome, ' + player_name + '! Your journey begins now!')

# Make the welcome message neater utlizing an f string.
print(f'Welcome {player_name}! Your jouney commences now!')

# Describe the Starting Area.
starting_area = '''In outer space awoke the adventurer. He is on a 
spaceship of course, shielded from the cold emptiness of space itself. 
Confused, he wonders through the ship knowing absolutley nothing. 
From the detection of his motion, a video begins to play on a screen. 
It is from a stranger telling him that he is the last surviving human 
from Earth and is currebtly heading to Mars.'''

print(starting_area)

# Ask the player for their first decision
decision = input("Do you wish to take the path? (yes or no): ").lower()

# Respond based on the player's decision
if decision == "yes":
    print(f"Brave choice, {player_name}! You step onto the path and venture forward.")
elif decision == "no":
    print(player_name + ", you decide to wait. Perhaps courage will find you later.") # Concatenation example
else:
    print("Confused, you stand still, unsure of what to do.")