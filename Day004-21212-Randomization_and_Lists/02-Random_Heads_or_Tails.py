"""
Function to generate the String 'Heads'
or 'Tails' randomly
"""
import random

binary = random.randint(0,1)
print(f"{'Heads' if binary == 1 else 'Tails'}")