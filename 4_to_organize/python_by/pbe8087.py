#!/usr/bin/env python3

def enterData(datadic):
    """Put data into a dictionary."""
    name = input("Enter your name:\n>> ")
    surname = input("Enter your surname:\n>> ")
    subject = input("Enter your favorite subject in school:\n>> ")
    postcode = input("Enter your postcode:\n>> ")
    datadic['name'] = name
    datadic['surname'] = surname
    datadic['subject'] = subject
    datadic['postcode'] = postcode

def nameSurnameLen(datadic):
    """Print the length of the name and surname."""
    print(f"\tName: {datadic['name']}")
    print(f"\tLength: {len(datadic['name'])}\n")
    print(f"\tsurname: {datadic['surname']}")
    print(f"\tLength: {len(datadic['surname'])}\n")

#TODO in: subject in school,    out: "-" between the letters

def spellingSubject(datadic):
    """Print slash in a word to emulate its spelling."""
    print(f"spelling:")

    string = datadic['subject']
    lim = len(string)

    for i in range(0,lim-1):
        print(string[i], end="-")

    print(string[lim-1], '\n')


#TODO in: valid typing in uppercase,    out: return the phrase

def validUpper():
    """Evaluate a phrase in uppercase."""
    phrase = input("Enter a phrase in uppercase:\n>> ")
    if phrase.isupper():
        print(f"Nice, you typed the {phrase} in uppercase!")
    else:
        print(f"Your phrase:\t{phrase}.\nIs not in uppercase.")

#TODO in: postcode,     out: first two words in uppercase

def postcodeUpper(datadic):
    """Print the first two words of a postcode in uppercase."""
    print(f"Your postcode is:")
    print(datadic['postcode'][0:2].upper() + datadic['postcode'][2:])

#TODO in: enter name,       out: len vowels

def nameVowelsLen(datadic):
    """Print the length of a name."""
    name = datadic['name']
    lim = len(name)
    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0

    for i in range(0,lim):
        if name[i] in vowels:
            count += 1

    print(f"\tName: {datadic['name']}",
            f"\n\tNumber of vowels: {count}\n")

#TODO in: enter pw,     out: valid

def pwValidation(datadic):
    """Validate a password."""
    while True:
        
        # input passwords
        pw1 = input("Enter your password or [q]uit:\n>> ")
        if pw1.lower() == 'q':
            break
        pw2 = input("Enter your password again or [q]uit:\n>> ")
        if pw2.lower() == 'q':
            break

        # verify matching
        if pw1 == pw2:
            datadic['password'] = pw1
            print("Your password was updated.")
            break
        elif pw1.lower() == pw2.lower():
            print("Your password must match the case.")
        else:
            print("Incorrect! The passwords don't match.")

#TODO in: enter word,   out: display backwards

def wordBackwards():
    """Print a given word in backwards."""
    word = input("Enter a word:\n>> ")
    length = len(word)
    count = 1

    for i in word:
        position = length - count
        print(word[position])
        count += 1

def printInfo(datadic):
    """Print your data."""
    print('Your current data is:\n--------------\n')
    for key, value in datadic.items():
        print(f"{key}: {value}")
    print("That's all!\n--------------\n")

def menu():
    """Print menu options."""
    print(
            f"\n\t[0] Show menu.",
            f"\n\t[1] Enter data your data.",
            f"\n\t[2] Enter a new password. ",
            f"\n\t[3] Show the length of the name and surname.",
            f"\n\t[4] Show the spelled format of your favorite subject in high school.",
            f"\n\t[5] Verify if a typo is in uppercase.",
            f"\n\t[6] Show the upper case of the first two words in your postcode.",
            f"\n\t[7] Show the number of vowels in your name.",
            f"\n\t[8] Show a word in backwards.",
            f"\n\t[9] Show your data.",
            f"\n\t[q] Quit the program.\n")

def main():
    """The main program."""
    print("Welcome to the UTILITIES PROGRAM.\n--------------------------------------\n")
    print("First, enter your data...\n")
    datadic = {}
    
    if not datadic:
        print("You don't have any data yet.\n")
        resp = input("Do you want to enter your data? [y]es or [n]o?\n>> ")
        resp = resp.lower()

        while True:
            if resp != 'y' and resp != 'n':
                print("\nInvalid option, please type [Y]es or [N]o.")
                resp = input(f">> ")
                resp = resp.lower()
            else:
                break

        if resp == 'n':
            print("Ok... See ya in the next time!")
        else:
            enterData(datadic)
            menu()
            while True:
                option = input("Choose an option:\n>> ")
                option = option.lower()
                if option == '0':
                    menu()
                elif option == '1':
                    enterData(datadic)
                elif option == '2':
                    pwValidation(datadic)
                elif option == '3':
                    nameSurnameLen(datadic)
                elif option == '4':
                    spellingSubject(datadic)
                elif option == '5':
                    validUpper()
                elif option == '6':
                    postcodeUpper(datadic)
                elif option == '7':
                    nameVowelsLen(datadic)
                elif option == '8':
                    wordBackwards()
                elif option == '9':
                    printInfo(datadic)
                elif option == 'q':
                    break
                else:
                    print("Invalid option, please select another one!")

# The main run of the program.
main()

