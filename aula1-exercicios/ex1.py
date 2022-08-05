# Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: 
# adição, subtração, multiplicação e divisão

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

adicao = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2

print(f"\nPrimeiro número = {num1}, Segundo número = {num2};")
print(f"Adição {num1} + {num2} = {adicao};")
print(f"Subtração {num1} - {num2} = {subtracao};")
print(f"Multiplicação {num1} * {num2} = {multiplicacao};")
print(f"Divisão {num1} / {num2} = {divisao};")