def get_num(msg):
    try:
        num = float(input(msg))
        return num
    except ValueError:
        print("Please enter a valid number")
        return get_num(msg)


def bid(current_bid):

    # get bid input
    new_bid = get_num("Enter your bid: ")

    # to finish bidding
    if new_bid <= 0:
        print("Bidding has finished")
        return current_bid

    # if bid isn't high enough
    elif new_bid <= current_bid:
        print("Please enter a higher bid")

    # if bid is valid
    elif new_bid > current_bid:
        current_bid = new_bid
        print(f"Current bid is at ${current_bid:.2f}")

    return bid(current_bid)


auction1_subject = input("Enter auction subject: ")
auction1_reserve = get_num("Enter reserve price: ")
print()

print(f"Auction for {auction1_subject} has begun.")
print(" To end the bid, enter any number below 1")
print()

auction1_bid = bid(0)
print()

if auction1_bid >= auction1_reserve:
    print(f"Reserve has been met.\n"
          f"The auction for the {auction1_subject} has finished "
          f"with a bid of ${auction1_bid:.2f}")
else:
    print(f"The reserve of ${auction1_reserve:.2f} for the {auction1_subject} "
          f"has not been met.")
