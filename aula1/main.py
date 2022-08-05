import math

if __name__ == '__main__':
    num1 = 123
    num2 = 3.3333333333
    letra = 'A'
    texto = "olá"
    print(num1)
    print(num2)
    print(letra)
    print(texto)
    print(num2.as_integer_ratio())


    idade = int(input("Informe a sua idade: "))

    if idade <= 18:
        print("Jovem")
    elif 18 < idade < 60:
        print("Adulto")
    else:
        print("Idoso")

    print("Sua idade *3: ", idade * 3)
    for i in range(3):
        print("Sua idade: ", idade)

    nome = input("Informe o seu nome: ")
    print("nome.upper()", nome.upper())
    print("nome.lower()", nome.lower())
    print("nome.capitalize()", nome.capitalize())
    print("nome[3:4]", nome[3:6])
    print("nome[2:]", nome[2:])
    print("nome.replace('br', '45')", nome.replace("br", "88"))
    print("nome.find('Ga')", nome.find("Ga"))
    print("len(nome)", len(nome))
    print("nome.strip()", nome.strip())
    print(f"Nome : {nome} | Idade: {idade}")

    n1 = 10
    n2 = 14
    print(f"n1: {n1}, n2: {n2}")
    print("soma = n1 + n2", n1 + n2)
    print("dif = n1 - n2", n1 - n2)
    print("mult = n1 * n2", n1 * n2)
    print("div = n1 / n2", n1 / n2)
    print("resto = n1 % n2", n1 % n2)
    print("exp = n1 ** n2", n1 ** n2)

    num3 = 49
    print("num3 = 49")
    print("math.sqrt(num3)", math.sqrt(num3))
    print("round((num3 / 1.13), 2)", round((num3 / 1.13), 2))
