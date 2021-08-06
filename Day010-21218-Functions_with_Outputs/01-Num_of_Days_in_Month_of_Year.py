# -*- coding: utf-8 -*-
"""
Program to find number of days in a month
Created on Fri Aug  6 22:32:32 2021

@author: divxd
"""


def format_name(fName, lName):
    return fName.title()+" "+lName.title()


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    numDays = month_days[month-1]
    if month == 2 and is_leap(year):
        numDays += 1
    return numDays


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
