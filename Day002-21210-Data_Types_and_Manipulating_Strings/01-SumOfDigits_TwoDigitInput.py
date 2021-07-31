# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 20:40:21 2021

@author: divxd
"""

two_digit_number = input("Type a two digit number: ")

sumDigits = int(int(two_digit_number)/10) + int(int(two_digit_number) % 10)
print(str(sumDigits))
