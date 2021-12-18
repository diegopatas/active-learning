from sys import argv

def process_content(filename):
    """Open and close a file."""
    open_op = open(filename)
    file_content = open_op.read()
    open_op.close()
    return  file_content

def erase_content(filename):
    """Erase the content of a file."""
    open_op = open(filename, 'w')
    open_op.truncate()
    open_op.close()

def write_content(filename):
    """Insert a content in an empty file."""
    open_op = open(filename, 'w')
    insert_line = input("Insert a line: ")
    open_op.write(f"{insert_line}\n")
    open_op.close()

def show_content(filename):
    """Print a file content."""
    open_op = open(filename)
    print(open_op)
    open_op.close()


# MAIN PROGRAM

script, filename = argv

print(f"Welcome! This is the current content of the file: "
      f"\n{filename.show_content()}")

resp = input("Do you want to erase the content? [Y]es or [N]o?")

if resp.lower() == 'n':
    filename.erase_content(filename)

while True:
    resp = input("Do you want to insert a line to the file? [Y]es or [N]o")
    if resp.lower(filename) == 'n':
        break
    else:
        filename.write_content(filename)

print(f"The final content of the file is: "
      f"\n{filename.show_content(filename)}.")
