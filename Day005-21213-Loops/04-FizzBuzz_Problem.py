# -*- coding: utf-8 -*-
"""
The FizzBuzz generator.
For 1 till 100, print Fizz if divisible by 3, Buzz if by 5, and FizzBuzz
if by both

Created on Sun Aug  1 15:50:08 2021

@author: divxd
"""

for num in range(1, 101):
    if num % 3 and num % 5:
        print("FizzBuzz")
    elif num % 3:
        print("Fizz")
    elif num % 5:
        print("Buzz")
    else:
        print(num)
