# Program AVERAGE
# INICIO
print("Olá humano, bem-vindo à Matrix!\n"
      "Calcule uma média de notas com esse programa...")

A = int(input("Informe a Nota 1: "))
B = int(input("Informe a Nota 2: "))
C = int(input("Informe a Nota 3: "))
D = int(input("Informe a Nota 4: "))

MD = (A + B + C + D)/4
if MD < 7:
    print("Você foi insuficiente, reles humano... Faça uma prova de exame.\n")
    NE = int(input("Informe a sua nota de Exame: "))
    NF = (MD + NE)/2
    if NF < 5:
        print("É, realmente você é humano e insuficiente! Boa sorte da próxima vez.")
    else:
        print("Parece que depois de tanto sofrimento você passou... Te espero na próxima.")
else:
    print("Boa garoto, dessa vez você passou...")

print(f"Sua média é: {MD}")