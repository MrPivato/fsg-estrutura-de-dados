# Crie uma lista contendo 20 valores numéricos, informados pelo usuário. 
# Com base na lógica de ordenação realizada em aula, no primeiro encontro, 
# ordene estes valores e os imprima em ordem crescente.

TAM_LISTA = 20
lista = []

for i in range(TAM_LISTA):
    lista.append(int(input(f"Informe o {i+1}° número: ")))

menor = lista[0]

for i in range(TAM_LISTA):
    for j in range(TAM_LISTA-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("\nSua lista organizada é: ", lista)

