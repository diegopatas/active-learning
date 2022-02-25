# Program to hand with movie tickets
message = "Welcome to the Movie Theater!\n"
message += "(Type 'quit' to exit)\n"
message += "Please, enter your age: "

age = ''
while age != 'quit':
    age = input(message)
    if age != 'quit':
        agenumb = int(age)
        if agenumb <= 4:
            price = 0
        elif agenumb <= 12:
            price = 10
        elif agenumb > 12:
            price = 15
        print(f"So you have {age}! Then your ticket costs: ${price}...")
    else:
        print("Thank you for using the program!")

while True:
    age = input(message)
    if age != 'quit':
        agenumbi = int(age)
    if age == 'quit':
        print("Thank you for using the program!")
        break
    elif agenumbi <= 4:
        price = 0
    elif agenumbi <= 12:
        price = 10
    elif agenumbi > 12:
        price = 15
    print(f"So you are {age} years old! Then, your ticket costs: ${price}...")