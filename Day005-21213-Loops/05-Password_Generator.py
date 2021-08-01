# -*- coding: utf-8 -*-
"""
Password Generator, using loops and random

Created on Sun Aug  1 17:05:16 2021

@author: divxd
"""

# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pwd = []

for i in range(nr_letters):
    pwd.append(random.choice(letters))

for i in range(nr_symbols):
    pwd.append(random.choice(symbols))

for i in range(nr_numbers):
    pwd.append(random.choice(numbers))

print("Before shuffling, the password is:")
for char in pwd:
    print(char, end="")
print()

random.shuffle(pwd)
print("After shuffling, the password is:")
for char in pwd:
    print(char, end="")
print()
