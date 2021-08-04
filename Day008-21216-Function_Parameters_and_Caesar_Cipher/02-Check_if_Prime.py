# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:27:41 2021

@author: divxd
"""


def prime_checker(number):
    """
    Function to check if a number is a prime.
    Prints the message to the console
    Parameters
    ----------
    number : integer

    Returns
    -------
    None.

    """
    for nums in range(2, number//2+1):
        if number % nums == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
