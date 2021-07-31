# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 23:13:09 2021

@author: divxd
"""

year = int(input("Which year do you want to check? "))

if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    print("Leap year.")
else:
    print("Not leap year.")
