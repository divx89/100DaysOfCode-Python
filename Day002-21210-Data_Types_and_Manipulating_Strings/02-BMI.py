# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 22:32:46 2021

@author: divxd
"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = int(float(weight) / (float(height) ** 2))
print(bmi)
