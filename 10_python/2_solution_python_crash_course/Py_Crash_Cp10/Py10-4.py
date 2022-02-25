# Program GUESTS BOOK
filename = 'guest_book.txt'

print("Hi! Welcome to the GUEST NOTEBOOK program.")

with open(filename, 'a') as f_obj:
    print("Please, enter your username (type 'q' to finish).")
    active = True
    while active:
        username = input("next user: ")
        if username == 'q':
            active = False
        else:
            f_obj.write(f"{username}\n")
with open(filename) as f_obj:
    content = f_obj.read()

print(content)
