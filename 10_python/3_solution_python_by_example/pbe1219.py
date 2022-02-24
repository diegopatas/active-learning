#!/usr/bin/env python3

def showBigger():
    """Show numbers in order, the smallest is shown first."""
    num_1 = int(input("Enter the first number:\n> "))
    num_2 = int(input("Enter the second number:\n> "))
    
    print(f"You have entered:")
    if num_1 < num_2:
        print(f"\t{num_1}\n\t{num_2}")
    else:
        print(f"\t{num_2}\n\t{num_1}")


def underTwenty():
    """Evaluate if a given number is under 20 or not."""
    num_eva = int(input("Enter a number under 20:\n> "))
    
    print("Let's see...\n")
    if num_eva < 20:
        print(f"Ok, the number you enter\n\t{num_eva}\n",
                f"is under the number 20.")
    else:
        print(f"Nope, the number\n\t{num_eva}",
                f"is too high!")


def likeColour():
    """Print a message about the red colour."""
    colour = input("Enter a colour;\n> ")
    if colour.lower() == 'red':
        print(f"I like {colour.lower()}, too!")
    else:
        print(f"I don't like {colour.lower()}, I like red!")


def ageCapability():
    """Print possibilities according to the age given."""
    age = int(input(f"Enter your age:\n> "))

    print(f"With {age} years old, you can...")
    if age >= 18:
        print(f"\n\t> Vote! Nice...")
    elif age >= 17:
        print(f"\n\t> Learn to drive, awesome!")
    elif age >= 16:
        print(f"\n\t> Buy a lottery ticket, amazing.")
    else:
        print(f"\n\t> go Trick-or-Treating.")

# main program

print(f"Welcome to the program: NUMBER ASSISTANT\n\n",
        f"You can explore it by using the following Menu.\n")

print(f"-----NUMBER ASSISTANT-----",
        f"Please, choose one option:\n...........")
print(f"\n\t[1] to Show two numbers in order.",
        f"\n\t[2] to Verify if a given number is under 20.",
        f"\n\t[3] to Opine over a given colour.",
        f"\n\t[4] to Say what you can do with a certain age.\n..........\n")

while True:
    
    option = int(input("Enter your option:[0] Menu [5] Quit\n> "))
    
    if option == 0:
        print(f"\n\t[1] to Show two numbers in order.",
                f"\n\t[2] to Verify if a given number is under 20.",
                f"\n\t[3] to Opine over a given colour.",
                f"\n\t[4] to Say what you can do with a certain age.",
                f"\n\t[5] to Quit.",
                f".........\n")
    elif option == 1:
        showBigger()
    elif option == 2:
        underTwenty()
    elif option == 3:
        likeColour()
    elif option == 4:
        ageCapability()
    elif option == 5:
        print(f"Thank you for test over bot! See ya!")
        break
    else:
        print("Invalid number, please enter a valid one!")

