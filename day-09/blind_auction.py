# Simple program to simulate a blind bidding auction

import clear_screen
import gavel_ascii

gavel = gavel_ascii.gavel
print(gavel)

bids = {}

add_more = True


def get_highest_bid(ledger):
    highest_bid = 0
    for bidder in ledger:
        bid_amount = ledger[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a highest bid of £{highest_bid}")


while add_more != False:
    bidder = input("What is your name?: ")
    bid = int(input("\nWhat is your bid?: £"))
    bids[bidder] = bid
    continue_input = input("\nAdd another bidder? Type 'yes' or 'no'.\n")
    clear_screen.clear()
    if continue_input == "no":
        add_more = False
        get_highest_bid(bids)
