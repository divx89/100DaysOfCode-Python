# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 12:14:09 2021

@author: divxd
"""

from math import ceil


def paint_calc(height, width, cover):
    """
    Function to find out how many paint cans are needed
    to paint a wall with given height and width
    Prints out the required information
    Parameters
    ----------
    height : float
          Height of the wall
    width : float
          Width of the wall
    cover : float
          Area covered by one can of paint
    
    Returns
    -------
    None.

    """
    numCans = ceil((height * width) / cover)
    print(f"You'll need {numCans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
