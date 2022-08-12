# Utilizando o for ou o while, ler 5 notas e informar a média

repet = 5
notas = 0

for i in range(repet):
    notas += float(input(f"Informe a nota {i+1}: "))

media = notas / repet
print(f"Sua média é: {media};")