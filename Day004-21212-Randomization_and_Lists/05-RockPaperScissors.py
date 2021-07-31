rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

hand = [rock,paper,scissors]
chosen = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")

try:
  choice = int(chosen)
  if choice < 0 or choice > 2:
    raise ValueError
  myChoice = hand[choice]
  compChoice = hand[random.randint(0,2)]

  print("You chose:")
  print(myChoice)
  print("The Computer chose:")
  print(compChoice)

  if myChoice == compChoice:
    print("It's a draw")
  elif [myChoice,compChoice] in [[rock,scissors],[paper,rock],[scissors,paper]]:
    print("You Win!")
  else:
    print("You lose")
except ValueError:
  print("Incorrect Input Value")