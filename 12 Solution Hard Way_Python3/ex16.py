"""
This program shows a file's content and gives the option to erase and/or insert new lines.
"""

from sys import argv

# Functions
def insert_line(file_name):
    """Insert lines to a file."""
    context = open(file_name, 'a')
    while True:
        resp = input("Do you want to insert a line? [y]es or [n]o?: ")
        if resp.lower() == 'n':
            break
        else:
            line = input("Type what you want to insert:\n")
            context.write(f"{line}\n")
    context.close()

def content_printing(file_name):
    """Print a file's content."""
    content_print = open(file_name, 'r')
    print(f"Now, the new file's content is:\n {content_print.read()}")
    content_print.close()

# Main program
script, filename = argv

print(f"Welcome to the 'Text-Insertion Script'!"
        f"What do you want to do?")
option = input("Do you want to [1] erase the file or [2] insert lines? ")
if option == '1':
    option_erase = open(filename, 'w')
    option_erase.close()
    print("The file was erased!\n See you!")
else:
    insert_line(filename)
    content_printing(filename)
    print("See you!")
