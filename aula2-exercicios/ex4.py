# Utilizando o for ou o while, ler um número inteiro entre 1 e 10 (validar), e
# imprimir a tabuada deste numero

num = 0

while num < 1 or num > 10:
    num = int(input("Informe um número entre 1 e 10: "))

print(f"Tabuada do {num}:")
for i in range(1, 11):
    print(f"{num}x{i} =\t{num*i}")