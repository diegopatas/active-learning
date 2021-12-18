# Programa para calcular velocidade média

# NOME DO PROGRAMA
print("programa STATUS de VEÍCULO")
# VAR
# INICIO
print("Digite a Velocidade Média da corrida e o Tempo total!")
Vmedia = float(input("VelocidadeMedia: "))
TempoTtl = float(input("TempoTotal: "))
DistanciaT = Vmedia*TempoTtl
Qlitros = DistanciaT/12
print("O relatório da viagem é exibido a seguir.\n")
print(f"\tTempo percorrido: {TempoTtl}.\n"
      f"\tVelocidade Média da viagem: {Vmedia}.\n"
      f"\tDistância total percorrida: {DistanciaT}.\n"
      f"\tQuantidade de combustível consumido, em litros: {Qlitros}.")
# FIM