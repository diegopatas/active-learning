# Program VERIFY NUMBER ATTEMPT
def verify_inclusion():
    """Verifies if a number is in a list from 1 to 9."""
    ver_num = int(input("Enter a number: "))
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if ver_num in list:
        print(f"The number {ver_num} is between 1 and 9.")
    else:
        print(f"The number {ver_num} isn't between 1 and 9.")
# INICIO
verify_inclusion()
