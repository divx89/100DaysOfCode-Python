# -*- coding: utf-8 -*-
"""
Higher Lower Game
Created on Tue Aug 10 12:51:17 2021

@author: divxd
"""
import art
import game_data
import random
import os


def clearConsole():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def update_scores(score, answerCorrect):
    if answerCorrect:
        score += 1
    return score


def update_options(options, isModify):
    if isModify:
        del options[0]
    options.append(random.choice(game_data.data))


def display_options(options, score, showScore=False, lost=False):
    clearConsole()
    print(art.logo)
    if showScore:
        print(f"You're right! Current score: {score}")
    elif lost:
        print(f"Sorry, that's wrong. Final score: {score}")
    if not lost:
        print(
            f"Compare A: {options[0]['name']}, a {options[0]['description']}, from {options[0]['country']}")
        print(art.vs)
        print(
            f"Against B: {options[1]['name']}, a {options[1]['description']}, from {options[1]['country']}")


def is_answer_valid(options, choice):
    if choice == 'A':
        is_Valid = options[0]['follower_count'] >= options[1]['follower_count']
    else:
        is_Valid = options[1]['follower_count'] >= options[0]['follower_count']
    return is_Valid


def game():
    options = []
    score = 0
    for i in range(0, 2):
        update_options(options, False)

    game_continues = True
    showScore = False
    while game_continues:
        display_options(options, score, showScore)
        while True:
            choice = input("Who has more followers? Type 'A' or 'B': ")
            if choice not in ['A', 'B']:
                print("Please enter the correct choice")
            else:
                break
        is_correct = is_answer_valid(options, choice)
        if is_correct:
            score += 1
            showScore = True
            update_options(options, True)
        else:
            game_continues = False
            display_options(options, score, False, True)
