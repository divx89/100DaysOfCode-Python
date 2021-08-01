# -*- coding: utf-8 -*-
"""
Take a list of scores, and find the highest score using loops
Created on Sun Aug  1 15:21:07 2021

@author: divxd
"""

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest = student_scores[0]
for score in student_scores:
    if score > highest:
        highest = score
print(f"The highest score in the class is: {highest}")
