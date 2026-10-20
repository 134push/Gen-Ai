bidding = {}
while True:
    name = input("Enter your name: ")
    bidding[name] = input("Enter your bid: $")
    user = input("You want to add another bidder? ")
    if user == "no":
        break
winner = ""
highest_bid = 0
for name, bid in bidding.items():
    bid = int(bid)
    if bid > highest_bid:
        highest_bid = bid
        winner = name
print(f"The winner is {winner} with a bid of ${highest_bid}")