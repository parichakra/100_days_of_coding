from turtle import clear


bids ={}

bidding_finish= False

def find_hightst_bidder(bidding_record):
    hightst_bid=0

    for bidders in bidding_record:
        bid_amount= bidding_record[bidders]
        if bid_amount> hightst_bid:
            hightst_bid=bid_amount
            winner =bidders
    print(f"the winner is {winner} with bid of {hightst_bid}")

while not bidding_finish:
    name= input("what is your name? :")
    price = int(input("what is your bid? :$"))
    bids[name]=price

    should_continue = input("Are there any other bidders? yes/no")

    if should_continue =="no":
        bidding_finish= True
        find_hightst_bidder(bids)
    elif should_continue =="yes":
        clear()
