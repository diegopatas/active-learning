#!/usr/bin/env python3

# main program
print(f"Welcome to the BILL CALC program!\n\t Ready to divide your bill?")
total = int(input("Enter the total:\n> "))
diner_num = int(input("Enter how many people ate:\n> "))

# dividebyzero validation
if diner_num != 0:
    total_per_person = total/diner_num
    print(f"The total for each person is: {total_per_person}.\nSee you!")
else:
    print(f"Nobody ate, so the discount is bigger! ;) ")

