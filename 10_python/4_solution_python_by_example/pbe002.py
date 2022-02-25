#!/usr/bin/env python3

def show_name(first, middle=None, last):
    """Print the first, the middle, and the last name."""
    first = input("Enter your first name:\n> ")
    middle = input("Enter your middle name:\n> ")
    last = input("Enter your last name:\n> ")
    print(f"Your name is: {first} {middle} {last}")

# main program

print(f"Welcome to the SHOW NAME program.")
first = input("Enter your first name:\n> ")
middle = input("Enter your middle name:\n> ")
last = input("Enter your last name:\n> ")

show_name(first, middle, last)

