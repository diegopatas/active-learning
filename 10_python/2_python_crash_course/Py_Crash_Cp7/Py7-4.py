# Program to loop into pizzas
prompt = "Please, add a topping to your pizza.\n"
prompt += "Type 'quit' if you want to exit the program."

pizza_entry = ""
while pizza_entry != 'quit':
    pizza_entry = input(prompt)
    print(pizza_entry)

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)