#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

EASY_LEVEL = 5
HARD_LEVEL = 10

def choose_difficulty():
  while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty in ['easy','hard']:
      break
    else:
      print("Please enter a correct value")

  return HARD_LEVEL if difficulty == 'easy' else EASY_LEVEL

def verify_guess(num,guess,numOfGuesses):
  if guess == num:
    print(f"You got it! The answer was {num}.")
    return -1
  else:
    print("Too","high" if guess > num else "low")
    numOfGuesses -= 1
  return numOfGuesses

def make_guess():
  while True:
    guess = input("Make a guess: ")
    try:
      guess = int(guess)
      break
    except:
      print("This guess is not an integer. Please retry.")
  return guess

def play_game():
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")

  num = randint(1,100)
  
  numOfGuesses = choose_difficulty()

  while numOfGuesses > 0:
    print(f"You have {numOfGuesses} attempts remaining to guess the number.")
    
    guess = make_guess()
    numOfGuesses = verify_guess(num,guess,numOfGuesses)

    if numOfGuesses == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != num:
      print("Guess again")

play_game()