# Program Rest
# INICIO
print("Olá de novo, humano. Esse programa é expresso e informa os valores divisíveis por 2 e por 3.")

list_num = []

active = True
while active:
    add_ver = input("Informe o valor a ser verificado (digite 'q' para sair): ")
    if add_ver == 'q':
        active = False
    elif add_ver != 'q':
        add = int(add_ver)
        list_num.append(add)

for ni in list_num:
    if (ni % 2 == 0) and (ni % 3 == 0):
        print(f"O número {ni} é divisível por 2 e por 3.")
    else:
        print(f"O número {ni} não atende a essa decisão... So sorry!")
