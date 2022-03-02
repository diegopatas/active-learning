#!/usr/bin/env python3

"""
Program: Utilities
Author: oitopatas
"""

# refactoring
def nameDic(): 
    """Stores the user name and surname."""
    fullname = {}
    name = input("Enter your name:\n>> ")
    surname = input("Enter your surname:\n>> ")
    fullname['name'] = name.lower()
    fullname['surname'] = surname.lower()
    return fullname

def nameLength(fullname):
    """Calculate a name's length."""
    print(f"Your name is {len(fullname['name'])} characters long, NICE!")

def nameSurname(fullname):
    """Concatenate a name with a surname."""
    print("Your full name is:\n", fullname['name']+" "+fullname['surname'], "\nAwesome...\n")
    print("Your full name's lenght is:",len(fullname['name']+fullname['surname']))

def titleName(fullname):
    """Title case a name."""
    print(f"Your title case name is {fullname['name'].title()}.\n\tCool, right?")

def pigLatin():
    """Print the pig latin exercise."""
    print("Translate a word to Pig Latin.\n")
    word = input("Enter a word:\n>> ").lower()
    alpha = ['a', 'e', 'i', 'o', 'u']
    print("Pig Latin Translation:\n")
    if word[0] not in alpha:
        print(word[1:]+word[0]+"ay")
    else:
        print(word+"way")

def menu():
    """Exibe the program's menu."""
    print("\nChoose an option:")
    print(f"\n\t[1] Enter your name and surname.",
            f"\n\t[2] Exibe the length of your name.",
            f"\n\t[3] Exibe your name and your surname.",
            f"\n\t[4] Title your name.",
            f"\n\t[5] Pig Latin Translation.",
            f"\n\t[6] Quit the program.\n")

def main():
    """Run de the main part of the program"""
    print("Welcome to the program NAME UTILITIES!\n\n----------------")
    menu()
    while True:
        option = input("Enter your option. [0] Menu [6] Quit.:\n>> ")
        if option == "0":
            menu()
        elif option == "1":
            fullname = nameDic()
        elif option == "2":
            nameLength(fullname)
        elif option == "3":
            nameSurname(fullname)
        elif option == "4":
            titleName(fullname)
        elif option == "5":
            pigLatin()
        elif option == "6":
            break
        else:
            print("Invalid option! Please select another one...")

main()
