# Program AVERAGE
# INICIO
print("Olá humano, bem-vindo à Matrix!\n"
      "Calcule uma média de notas com esse programa...")

A = int(input("Informe a Nota 1: "))
B = int(input("Informe a Nota 2: "))
C = int(input("Informe a Nota 3: "))
D = int(input("Informe a Nota 4: "))

MD = (A + B + C + D)/4
if MD < 5:
    print("Senta e chola, você foi reprovado!")
else:
    print("Boa garoto, dessa vez você passou...")

print(f"Sua média é: {MD}")