# (Desafio) Ler 3 pontos dispostos em um plano cartesiano, ou seja, para cada
# ponto, deverão ser obtidos os valores de x e y. Ou seja, pares de (x1, y1), (x2,
# y2) e (x3, y3). De posse destes valores, verificar se estas coordenadas foram um
# triângulo.

pontos = []

print("\nInforme seus pares de pontos na notação x, y \nExemplo: 3, 7")

for i in range(3):
    ponto = input(f"Informe o par de pontos (x{i+1}, y{i+1}): ")

    par_ponto = []
    for j in ponto.split(","):
        par_ponto.append(int(j))

    pontos.append(par_ponto)

print()

# descobrir o coeficiente angular, m = (y2 - y1) / (x2 - x1)
m = (pontos[1][1] - pontos[0][1]) / (pontos[1][0] - pontos[0][0])
# descobrir o coeficiente linear, n = y - mx
n = pontos[0][1] - (m * pontos[0][0])

# se os 3 pontos estiverem na mesma reta, não é um triangulo
pontos_iguais = 0
for i in pontos:
    y = m * i[0] + n  # y = mx + n
    if i[1] == y:
        pontos_iguais += 1

if  pontos_iguais < 3:
    print("Seus pontos formam um triângulo!")
else:
    print("Seus pontos NÃO formam um triângulo!")