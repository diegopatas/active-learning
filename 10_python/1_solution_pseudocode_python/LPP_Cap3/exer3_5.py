# Programa para calcular o valor de uma prestação
# NOME DO PROGRAMA
print("Programa CÁLCULO DE PRESTAÇÃO EM JUROS SIMPLES.\n")
# Var
# INICIO
tempoTotal = float(input("Digite o prazo da prestação: "))
taxaAplicada = float(input("Digite o valor da taxa: "))
valorBem = float(input("Digite o valor: "))
prestBem = valorBem + (valorBem*(taxaAplicada/100)*tempoTotal)
print(f"\nO relatório da prestação segue abaixo!\n")
print(f"\tO valor da prestação é de: {prestBem}\n\n"
      "Obrigado por usar o nosso programa!")
# FIM