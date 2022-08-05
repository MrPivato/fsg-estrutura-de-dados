# Considerando que um veículo faz 14,5 km/l e que o custo de 1 l 
# de combustível seja R$ 5,26. Ler os seguintes valores:
# - Tempo da viagem
# - Velocidade média
# Apresentar o que segue:
# - Velocidade média
# - Tempo gasto na viagem
# - Distância percorrida
# - Quantidade de litros utilizada na viagem
# - Valor gasto em combustível

KM_POR_LITRO = 14.5
VALOR_POR_LITRO = 5.26

tempViagem = float(input("Informe o tempo da viagem (horas): "))
velMedia = float(input("Informe a velocidade média da viagem (km/h): "))

distPercorrida = tempViagem * velMedia
litrosGastos = round(distPercorrida / KM_POR_LITRO, 2)
valorGastos = round(litrosGastos * VALOR_POR_LITRO, 2)

print(f"\nVelocidade média: {velMedia} km/h;")
print(f"Tempo gasto na viagem: {tempViagem} horas;")
print(f"Distância percorrida: {distPercorrida} km;")
print(f"Quantidade de litros utilizada na viagem: {litrosGastos} litros;")
print(f"Valor gasto em combustível: R$ {valorGastos}")