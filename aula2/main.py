var_bool_1 = True
var_bool_2 = False
var_bool_3 = False

print(var_bool_1, var_bool_2, var_bool_3)
print(var_bool_1 and var_bool_2 and var_bool_3)
print(var_bool_1 & var_bool_2 & var_bool_3)

var_bool_4 = var_bool_1 and var_bool_2

print("'var_bool_1' e 'var_bool_2' são iguais é", var_bool_4)
print(var_bool_1 or var_bool_2 or var_bool_3)
print(var_bool_1 | var_bool_2 | var_bool_3)

var_bool_5 = var_bool_1 or var_bool_2 or var_bool_3

print(var_bool_5)
print("'var_bool_1' ou 'var_bool_2' ou 'var_bool_2' é igual a", var_bool_5)
print(not var_bool_1)

print("==================================")

var_int_1 = 5
var_int_2 = 10

print(var_int_1 == var_int_2)
print(var_int_1 != var_int_2)
print(var_int_1 > var_int_2)
print(var_int_1 < var_int_2)
print(var_int_1 >= var_int_2)
print(var_int_1 <= var_int_2)

print("==================================")

var_int_1 = 5
var_int_2 = 10

# estrutura condicional simples
if var_int_1 < var_int_2:
    print("'var_int_1' é menor do que 'var_int_2'")

# estrutura condicional composta
if var_int_1 > var_int_2:
    print("'var_int_1' é maior")
else:
    print("'var_int_1' não é maior")

x = 1
y = 5
if (x > 1) and (y % 2 == 0):
    print('x é maior que 1 e y é par')
else:
    print('Uma ou nenhuma das condições foram satisfeitas')

print("==================================")

lista = []  # ou lista = list()
print(lista)
lista = [1234, "Carro", 3.1415, False]
print(lista)
outralista = ["Avião", lista]
print(outralista)
print(outralista[1])

print("==================================")

nomes = ["Petros", "Laura", "Luís"]
for i in nomes:
    print(i)
else:
    print("Fim")

print("==================================")

soma = 0
for numero in range(1, 10):
    soma += numero
print(soma)
