# Utilizando a biblioteca math, ler dois números de ponto flutuante
# e efetuar as seguintes operações: exponenciação, raiz quadrada,
# arredondamento para 2 casas decimais da divisão entre os números

from cmath import sqrt
import math

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))

exponenciacaoNum1 = pow(num1, num2)
exponenciacaoNum2 = pow(num2, num1)
raizQuadradaNum1 = math.sqrt(num1)
raizQuadradaNum2 = math.sqrt(num2)
arred2Casas1 = round((num1 / num2), 2)
arred2Casas2 = round((num2 / num1), 2)

print(f"\nPrimeiro número = {num1}, Segundo número = {num2};")
print(f"Exponenciação Primeiro número {num1} ^ {num2} = {exponenciacaoNum1};")
print(f"Exponenciação Segundo número {num2} ^ {num1} = {exponenciacaoNum2};")
print(f"Raiz Quadrada Primeiro número math.sqrt({num1}) = {raizQuadradaNum1};")
print(f"Raiz Quadrada Segundo número math.sqrt({num2}) = {raizQuadradaNum2};")
print(f"Arredondamento para duas casas {num1} / {num2} = {arred2Casas1};")
print(f"Arredondamento para duas casas {num2} / {num1} = {arred2Casas2};")
