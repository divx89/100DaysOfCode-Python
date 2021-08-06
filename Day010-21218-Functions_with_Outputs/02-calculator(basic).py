# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 00:20:02 2021

@author: divxd
"""

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return (n1 / n2 if n2 != 0 else None)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))

    for operation in operations:
        print(operation)

    should_continue = True

    while should_continue:
        symbol = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        answer = operations[symbol](num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, 'n' to restart with a new set of numbers, or 'x' to exit the program: ")

        if choice == 'y':
            num1 = answer
        elif choice == 'n':
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
