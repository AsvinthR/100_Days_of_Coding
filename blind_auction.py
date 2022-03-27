import os
os.system ("cls")
from utilities_logos import blind_auction_logo

print(blind_auction_logo)

all_bids = {}

should_end = False
while not should_end:
    name = input("What is your name?\n")
    bid = input("What is your bid?\n")
    all_bids[name] = bid

    end_game = input("Are there other bidders to add? Yes or No \n").lower()
    os.system ("cls")
    if end_game == "no":
        should_end = True
        max_bidder = max(all_bids, key=all_bids.get)
        print(f"The winner is {max_bidder} with a bid of ${all_bids[max_bidder]}.")