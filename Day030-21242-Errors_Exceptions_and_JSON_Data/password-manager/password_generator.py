# -*- coding: utf-8 -*-
"""
Password Generator, using loops and random

Created on Sun Aug  1 17:05:16 2021

@author: divxd
"""

# Password Generator Project
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_pwd():
    pwd = []

    pwd.extend([random.choice(letters) for _ in range(random.randint(8, 10))])
    pwd.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    pwd.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(pwd)
    return ''.join(pwd)
