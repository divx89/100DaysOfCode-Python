# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:36:40 2021

@author: divxd
"""

# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")

total_bill = input("What was the total bill? $")
tip_pc = input("What percentage tip would you like to give? 10, 12, or 15? ")
split_bw = input("How many people to split the bill? ")

bill_amt = float(total_bill)
tip_calc = (float(tip_pc)/100) + 1
num_of_people = int(split_bw)

each_to_pay = "{:.2f}".format(round((bill_amt / num_of_people) * tip_calc, 2))
print(f"Each person should pay: ${each_to_pay}")
