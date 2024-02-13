from art import logo

print(logo)
bidders = []
more_bidders = True


def add_bidder():
    bidder = {}
    name = input("What is your name?\n")
    bid = input("What is your bid?\n$")
    bidder['name'] = name
    bidder['bid'] = bid
    bidders.append(bidder)


def choose_winner(bidders_b):
    winner = ""
    biggest_bid = 0
    for i in bidders_b:
        if int(i['bid']) > biggest_bid:
            biggest_bid = int(i['bid'])
            winner = (i['name'])
    print(f"The winner is {winner} with the bid ${biggest_bid}.")


while more_bidders:
    add_bidder()
    print("\n" * 100)  # simulate a clear effect
    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more == 'yes':
        more_bidders = True
    else:
        more_bidders = False
        choose_winner(bidders)
