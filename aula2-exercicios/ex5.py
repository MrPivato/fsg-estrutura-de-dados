# Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os
# armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
# para somar todos os valores digitados

lista = []

for i in range(5):
    lista.append(int(input(f"Informe o {i+1}° número: ")))

soma = 0
for i in lista:
    soma += i

print(f"A soma de sua lista é de: {soma};")