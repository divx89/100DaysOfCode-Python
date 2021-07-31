# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:33:27 2021

@author: divxd
"""

age = input("What is your current age?")

yearsLeft = 90 - int(age)
daysLeft = round(yearsLeft * 365)
weeksLeft = round(yearsLeft * 52)
monthsLeft = round(yearsLeft * 12)

print(
    f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")
