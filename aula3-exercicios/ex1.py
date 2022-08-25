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

# verifica maior e catetos
if d12 > d13 and d12 > d23:
    maior = d12
    c1 = d13
    c2 = d23
elif d13 > d12 and d13 > d23:
    maior = d13
    c1 = d12
    c2 = d23
else:
    maior = d23
    c1 = d12
    c2 = d13

# verifica qual tipo de triangulo
if d12 == d13 and d13 == d23:
    print('O triângulo é equilátero!')
elif d12 == d13 or d13 == d23 or d12 == d23:
    if round(maior**2,4) == round(c1**2,4) + round(c2**2,4):
        print('O triângulo é retângulo e isósceles!')
    else:
        print('O triângulo é isósceles!')
elif maior**2 == c1**2 + c2**2:
    print('O triângulo é retângulo!')
else:
    print('O triângulo é escaleno!')