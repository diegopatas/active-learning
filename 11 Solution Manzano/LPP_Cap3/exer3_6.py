# Programa para realizar a troca de valores entre variáveis
# INICIO
# entrada
print(f"Programa EFETUA TROCA DE VALORES DE VARIÁVEIS\n")
A = float(input("Digite o primeiro valor: "))
B = float(input("Digite o segundo valor: "))
print(f"\nO primeiro valor digitado foi {A}\n"
      f"O segundo valor digitado foi {B}\n")
# processamento
AUX = A
A = B
B = AUX

# saída
print(f"\tAgora o primeiro valor é {A}\n"
      f"\tE o segundo valor é {B}")
# FIM