# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 15:10:47 2021

@author: divxd
"""

from art import logo
import os


def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


bids = {}
continueBidding = 'yes'
print(logo)

while continueBidding == 'yes':
    name = input("What is your name? ")
    bid = float(input("What's your bid? $"))
    bids[name] = bid

    continueBidding = input(
        "Are there any other bidders? Type 'yes' or 'no'. ")

    clearConsole()

maxBid = [None, -1]
for bidder in bids:
    if maxBid[1] < bids[bidder]:
        maxBid = [bidder, bids[bidder]]
print(f"The winner is {maxBid[0]} with a bid of ${maxBid[1]}.")
