#!/usr/bin/env python3

# main program

print(f"Welcome to HOUR program.",
        f"Do you want to know how many seconds, minutes and hours a particular day has? So please...\n")

day = int(input("Enter the day:\n> "))
hours = day*24
minutes = hours*60
seconds = minutes*60

print(f"{day} days has:\n",
        f"\t{hours} hours\n",
        f"\t{minutes} minutes\n",
        f"\t{seconds} seconds...\n\n",
        f"That's all! See you ;) ")
