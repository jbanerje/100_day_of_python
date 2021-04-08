# Secret Auction Bid

import os
import art

bidders_list = []

def chk_highest_bidder():
    '''Function to check highest bidder based on higest bidding prices'''
    base_line_bid = 0
    winner = ''
    for bid in bidders_list:
        if bid['price'] > base_line_bid:
            base_line_bid = bid['price']
            winner_name = bid['name']
    return base_line_bid, winner_name

def update_dict(bidder_name, bidding_price):
    '''Function to Update Bidding List with bidders and prices'''
    bidders_list.append({'name':bidder_name, 'price':bidding_price})
    return

if __name__ == "__main__":

    print(art.logo)
    
    loop_thru_bidders = True

    while loop_thru_bidders == True:
        bidder_name = input('Bidder Name : ')
        bidding_price = float(input('Bidding Price : '))
        
        # Function to Update Bidding
        update_dict(bidder_name, bidding_price)
        
        input_more_bidders = input('Do we have more bidders (Y/N) :')
        
        if input_more_bidders == 'N':
            loop_thru_bidders = False
        
        clear = lambda: os.system('cls')
        clear()
    
    # Function to find clear winner
    base_line_bid, winner_name = chk_highest_bidder()

    print(f'Winner - {winner_name}, Price - {base_line_bid}')    
