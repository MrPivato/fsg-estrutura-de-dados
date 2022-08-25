# Complementar o exercício sobre a formação do triangulo, informando
# qual o tipo de triangulo que se formou.

import math

x1 = float(input("Digite coordenada x1 "))
y1 = float(input("Digite coordenada y1 "))
x2 = float(input("Digite coordenada x2 "))
y2 = float(input("Digite coordenada y2 "))
x3 = float(input("Digite coordenada x3 "))
y3 = float(input("Digite coordenada y3 "))
# Calcula a distancia entre os pontos
d12 = math.sqrt((x1-x2)**2 + (y1-y2)**2)
d13 = math.sqrt((x1-x3)**2 + (y1-y3)**2)
d23 = math.sqrt((x2-x3)**2 + (y2-y3)**2)

if d12 > abs(d13-d23) and d12 < d13+d23 and d13 > abs(d12-d23) and d13 < d12+d23 and d23 > abs(d12-d13) and d23 < d12+d13:
    if d12 == d13 == d23:
        print("Equilátero")
else:
    print('Estes pontos não formam um triângulo, formam uma reta ou estão sobrepostos!')
