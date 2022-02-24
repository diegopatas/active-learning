# Program Difference
A = ''
B = ''

# INICIO

print("Olá, humano!\n"
      "Aqui você consegue obter a diferenção do maior número dado pelo menor.")
A = float(input("Informe o primeiro valor: "))
B = float(input("Informe o segundo valor: "))

#PROCESSAMENTO
if A > B:
    result = A - B
else:
    result = B - A

print("O resultado da operação é: ")
print(result)
