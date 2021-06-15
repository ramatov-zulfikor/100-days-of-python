from replit import clear
from art import logo

print(logo)

print("Hello! Welcome to Blind Auction.")

any_bidders = True
bidders = {}

while any_bidders:
    name = input("What is your name?\n")
    bid = int(input("What is your bid? \n$"))

    bidders[name] = bid

    is_any_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'\n").lower()
    clear()

    if is_any_bidders == "no":
        any_bidders = False

highest_bidder = ""
highest_bid = 0

for key in bidders:
    if bidders[key] > highest_bid:
        highest_bidder = key
        highest_bid = bidders[key]

print(f"The winner is {highest_bidder.capitalize()} with a bid ${highest_bid}")
