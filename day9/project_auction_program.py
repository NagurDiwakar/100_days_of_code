print("Welcome to secret auction program")
bidders = input("Are they are any bidders Type 'yes' or 'no' ")

# to print a blank screen we can print(\n * 100 ) and ask for input might help

# importantluy we can consider each person name as key and bid as value into the dictionary

bidding_dictionary = {}
if bidders == "yes":
    name = input("what is ur name ? ")
    bid_amount = int(input("what's your bid ? : "))
    

    bidding_dictionary[name] = bid_amount
    print(bidding_dictionary)
elif bidders == "no":
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")