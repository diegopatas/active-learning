# Program ADD MATRIZES
def elab_list():
    list_N = []
    active = ''
    while active != 'q':
        elem = input(f"Enter a value: ")
        if elem != 'q':
            list_N.append(int(elem))
        else:
            active = 'q'
    return list_N

def copy_list(list_old: list, list_new: list):
    while list_old:
        elem = list_old.pop()
        list_new.append(elem)

list_A = elab_list()
list_B = elab_list()
list_C = []

copy_list(list_A[:], list_C)
copy_list(list_B[:], list_C)
print(f"Lista A: {list_A}\n Lista B: {list_B}\n Lista C: {list_C}")