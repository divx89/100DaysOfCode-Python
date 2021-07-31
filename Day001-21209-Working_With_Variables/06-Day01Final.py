# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 20:57:39 2021

@author: divxd
"""

#Day 001 - 06 - Day01Final

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator.")
#2. Ask the user for the city that they grew up in.
cityName = input("What's the name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
petName = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
newBandName = cityName + " " + petName;
print("Your band name could be " + newBandName)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/