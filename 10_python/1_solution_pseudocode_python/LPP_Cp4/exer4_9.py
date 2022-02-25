# Program MAX MIN
def read_values():
    """Read a value from the user"""
    num_list = []
    active = ''
    while active != 'q':
        verif = input("Enter a value: ")
        if verif == 'q':
            active = 'q'
        else:
            add_number = int(verif)
            num_list.append(add_number)
    return num_list

def show_min_max(list_evaluated):
    """Get the minimum and maximal value in a list"""
    MAX_var = list_evaluated[0]
    MIN_var = list_evaluated[0]
    for n_i in list_evaluated:
        print(n_i)
        if n_i > MAX_var:
            MAX_var = n_i
        elif n_i < MIN_var:
            MIN_var = n_i
    print(f"Max value: {MAX_var}, Min value: {MIN_var}")

# INICIO
list_evaluated = read_values()
show_min_max(list_evaluated)