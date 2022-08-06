# Ler 3 pontos dispostos em um plano cartesiano. Para cada ponto,
# deverão ser obtidos os valores de x e y. Ou seja,
# pares de (x1, y1), (x2, y2) e (x3, y3).

print("Informe seus pares de pontos na notação x, y \nExemplo: 3, 7\n")

ponto = input("Informe o primeiro par de pontos: ")
pontos = ponto.split(",")

ponto = input("Informe o segundo par de pontos: ")
pontos += ponto.split(",")

ponto = input("Informe o terceiro par de pontos: ")
pontos += ponto.split(",")

n = 1
print("\nSeus pontos são: ")
for i in range(0, int(len(pontos)), 2):
    print(f"(x{n}, y{n}) = ({pontos[i].strip()}, {pontos[i+1].strip()});")
    n += 1
    
