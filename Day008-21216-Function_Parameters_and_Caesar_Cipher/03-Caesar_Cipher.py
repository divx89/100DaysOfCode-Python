# -*- coding: utf-8 -*-
"""
Caesar Cipher Program
Created on Wed Aug  4 14:07:19 2021

@author: divxd
"""

from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    """
    Function to encode or decode a string using the caesar cipher method
    Prints the encoded or decoded string

    Parameters
    ----------
    start_text : String
        Text to be encoded or decoded
    shift_amount : integer
        Amount by which a text is to be shifted for encoding or decoding
    cipher_direction : String (Enumerated)
        encode/decode: whether to encode the string or decode it

    Returns
    -------
    None.

    """
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            end_text += alphabet[alphabet.index(char) + shift_amount]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")


print(logo)

answer = "yes"
while answer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(start_text=text, shift_amount=shift %
           26, cipher_direction=direction)

    answer = input(
        "Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
