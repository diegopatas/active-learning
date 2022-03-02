# Program WRITE THE USER'S NAME
filename = 'guest.txt'

print("Welcome to the WRITE NAME program.")
username = input("Please, enter your name: ")

with open(filename, 'w') as file_obj:
    file_obj.write(username)

with open(filename) as file_obj:
    content = file_obj.read()

print(content)