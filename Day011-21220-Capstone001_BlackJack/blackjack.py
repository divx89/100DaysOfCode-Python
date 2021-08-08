# -*- coding: utf-8 -*-
"""
Capstone Project 01 - Day 011 - Blackjack
Created on Sat Aug  7 22:35:27 2021

@author: divxd
"""

import random
from art import logo
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def deal_card(cards,oneOrTwo = 1):
    deal = []
    for i in range(oneOrTwo):
        deal.append(cards[random.randint(0, 12)])
    return deal

def calc_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score -= 10
    return score

def show_status(yourStatus, compStatus, final = False):
    if final:
        print(f"\tYour final hand: {yourStatus[0]}, final score: {yourStatus[1]}")
        print(f"\tComputer's final hand: {compStatus[0]}, final score: {compStatus[1]}")
    else:
        print(f"\tYour cards: {yourStatus[0]}, current score: {yourStatus[1]}")
        print(f"\tComputer's first card: {compStatus[0][0]}")

def comp_play(yourStatus, compStatus):
    yourScore = yourStatus[1]
    compScore = compStatus[1]
    compCards = compStatus[0]
    
    while True:
        if compScore == 21:
            show_status(yourStatus,compStatus,True)
            print("You lose. Other player has a blackjack")
            break
        elif compScore > 21:
            show_status(yourStatus,compStatus,True)
            print("Opponent went over. You win")
            break
        elif (21 - compScore) == (21 - yourScore):
            show_status(yourStatus,compStatus,True)
            print("Draw")
            break
        elif (21 - compScore) < (21 - yourScore):
            show_status(yourStatus,compStatus,True)
            print("You lose")
            break
        else:
            compCards.extend(deal_card(cards,1))
            compScore = calc_score(compCards)
            compStatus = [compCards,compScore]

while True:

    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'y':
        print("Thanks for trying out Blackjack! Bye!")
        break

    clearConsole()
    print(logo)

    compCards = deal_card(cards,2)
    compScore = calc_score(compCards)
    
    yourCards = []
    yourScore = 0
        
    while True:
        yourCards.extend(deal_card(cards,(1 if len(yourCards)!=0 else 2)))
        yourScore = calc_score(yourCards)
        
        yourStatus = [yourCards,yourScore]
        compStatus = [compCards,compScore]
        show_status(yourStatus,compStatus,False)
        
        if yourScore >= 21 or compScore >= 21:
            break
        
        if input("Type 'y' to get another card, type 'n' to pass: ") != 'y':
            break
    
    if yourScore >= 21:
        show_status(yourStatus,compStatus,True)
        if yourScore == 21:
            print("Win with a blackjack!")
        else:
            print("You went over. You lose")
        continue
    
    comp_play(yourStatus, compStatus)
    