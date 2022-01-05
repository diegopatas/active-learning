#!/usr/bin/env python3

print("Welcome to the ORDER NUMBERS program.\n This program puts given numbers in order.")

num1 = float(input("Enter the first number:\n> "))

num2 = float(input("Enter the second number:\n> "))

if num1 > num2:
    print(f"The order is:\n\t{num2}\n\t{num1}")
else:
    print(f"The order is:\n\t{num1}\n\t{num2}")

