# Import necessary modules
from replit import clear  # Used for clearing the console
import art  # Used for displaying ASCII art

# Display the auction logo and welcome message
print(art.logo)
print('Welcome to the secret auction program.\n')

# Initialize a dictionary to store bidder names and their bids
bidders_dict = {}

# Define a function to add a new bidder entry to the dictionary
def new_entry(bidder_name, bid_value):
    bidders_dict[bidder_name] = bid_value

# Main loop to collect bidder information
while True:
    # Prompt for and collect bidder's name and bid
    name = input('What is your name?: ')
    bid = int(input("What's your bid?: $"))
    # Add the new bidder to the dictionary
    new_entry(name, bid)

    # Ask if there are more bidders and break the loop if there are none
    others = input("Are there any other bidders? Type 'yes' or 'no': ")
    if others == 'no':
        break
    # Clear the console for the next bidder to maintain secrecy
    clear()

# Initialize variables to track the highest bid and bidder
highest_bid = 0
highest_bidder = ""

# Iterate through the dictionary to find the highest bid
for bidder, bid in bidders_dict.items():
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

# Clear the console before announcing the winner
clear()

# Announce the winner and their bid
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
