# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print(f"Copying from {from_file} to {to_file}.")
#
# in_file = open(from_file)
# indata = in_file.read()
#
# print(f"Does the output file exists? {exists(to_file)}.")
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# out_file.close()
# in_file.close()

"""
This program copy the content of a file to another one.
"""
from sys import argv
from os.path import exists

# Functions
def copy_content(from_file, to_file):
    """Copy the content of a file to another."""
    # origin file content copy
    file_copy = open(from_file)
    target_content = file_copy.read()

    # target file writing
    action = open(to_file, 'w')
    action.write(target_content)

    # closing step
    file_copy.close()
    action.close()

# Main
# VAR area
script, from_file, to_file = argv

# program
print("Welcome to the 'Copy Content Program'!\n")

if exists(to_file) == True:
    print(f"The file {to_file} already exists.\n")
    resp = input("Do you want to overwrite it? (Y/N): ")
    if resp.lower() == 'y':
        copy_content(from_file, to_file)
        print(f"Everything has been done!")
else:
    copy_content(from_file, to_file)
    print(f"Everything has been done!")

print(f"\n\tSee you!")
