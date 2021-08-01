# -*- coding: utf-8 -*-
"""
Summing up all even numbers between 1 and 100 using loops and range
Created on Sun Aug  1 15:35:55 2021

@author: divxd
"""

total = 0
for num in range(2, 101, 2):
    total += num
print(f"The sum of all even numbers between 1 and 100 is {total}")
