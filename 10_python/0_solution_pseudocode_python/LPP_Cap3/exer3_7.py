# Programa para Eleição
# INICIO
print(f"Programa PERCENTUAL DE VOTOS")
# ENTRADA
print(f"Informe primeiramente os votos válidos.\n")
A = float(input(f"Digite os votos do candidato A: "))
B = float(input(f"Digite os votos do candidato B: "))
C = float(input(f"Digite os votos do candidato C: "))
print(f"\nAgora informe os votos brancos e nulos!\n")
Bra = float(input(f"Digite os votos brancos: "))
N = float(input(f"Digite os votos nulos: "))
# PROCESS
totalVotos = A + B + C + Bra + N
perValidos = (A+B+C)/totalVotos

perA = (A/totalVotos)*100
perB = (B/totalVotos)*100
perC = (C/totalVotos)*100
perBra = (Bra/totalVotos)*100
perN = (N/totalVotos)*100
# SAIDA
print(f"Confira os percentuais da votação!\n"
      f"\tTotal de votos: {totalVotos}.\n"
      f"\tPercentual de votos válidos: {perValidos}%.\n"
      f"\tPercentual de votos do candidato A: {perA}%.\n"
      f"\tPercentual de votos do candidato B: {perB}%.\n"
      f"\tPercentual de votos do candidato C: {perC}%.\n"
      f"\tPercentual de votos em branco: {perBra}%.\n"
      f"\tPercentual de votos nulos: {perN}%.")