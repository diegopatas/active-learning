#!/usr/bin/env python3

"""
Program: Utilities
Author: oitopatas
"""

# refactoring
def nameSurname():
    """Stores the user name and surname."""
    name = input("Enter your name:\n>> ")
    surname = input("Enter your surname:\n>> ")
    fullname = []
    fullname.append(name)
    fullname.append(surname)
    return fullname
#TODO: continue from here
def nameLength(fullname: list):
    """Calculate a name's length."""
    print(f"Your name is {len(fullname[0])} characters long, NICE!")

def nameSurname():
    """Concatenate a name with a surname."""
    name = input("Enter your first name:\n>> ")
    surname = input("Enter your surname:\n>> ")
    print("Your full name is ", name+""+surname, "Awesome...")
    print("Your full name's lenght is ",len(name+surname))

def titleName():
    """Title case a name."""
    name = input("Enter your name:\n>> ")
    surname = input("Enter your surname\n>> ")
    print(f"Your title case name is {name.title()}.\nCool, right?")


