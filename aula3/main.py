# Listas: Lista é uma coleção de valores indexada, em que cada valor é identificado por
# um índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e assim por
# diante.

# • Tuplas: Tupla é uma estrutura de dados semelhante a lista. Porém, ela tem a
# característica de ser imutável, ou seja, após uma tupla ser criada, ela não pode ser
# alterada.

# • Dicionários: Os dicionários representam coleções de dados que contém na sua
# estrutura um conjunto de pares chave/valor, nos quais cada chave individual tem um
# valor associado. Esse objeto representa a ideia de um mapa, que entendemos como uma
# coleção associativa desordenada. A associação nos dicionários é feita por meio de uma
# chave que faz referência a um valor.

# • Conjuntos (set): Um Set (conjunto) é uma coleção não-ordenada de valores únicos,
# empregada para armazenar múltiplos itens em um objeto.


# COLEÇÕES - TUPLAS:
# As tuplas devem ser usadas em situações em que não haverá necessidade de
# adicionar, remover ou alterar elementos de um grupo de itens. Exemplos bons
# seriam os meses do ano, os dias da semana, as estações do ano etc. Nesses
# casos, não haverá mudança nesses itens.
dias_semana = ('Domingo', 'Segunda-feira', 'Terça-feira',
               'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado')
print(dias_semana)
print(dias_semana.index('Quinta-feira'))
print(dias_semana[2])
for ds in dias_semana:
    print(ds)

print("============================================================")

# COLEÇÕES - LISTAS:
# Lista é uma coleção de valores indexada, em que cada valor é identificado por
# um índice. O primeiro item na lista está no índice 0, o segundo no índice 1 e
# assim por diante.Para criar uma lista com elementos deve-se usar colchetes e
# adicionar os itens entre eles separados por vírgula, ou utilizar a função list().
# Lista.append(elemento) – adiciona o elemento a lista
# Lista.remove(elemento) – elimina o elemento da lista
medicos = ['Sandra', 'Pablo', 'Guilherme']
medicos.append('Salvador')
print(medicos)
medicos.remove('Pablo')
print(medicos)

programadores = ['Petros', 'Laura', 'Luís']
medicos = ['Sandra', 'Pablo', 'Guilherme']
todos = programadores + medicos
print(programadores)
print(medicos)
print(todos)
duplicados = todos * 2
print(duplicados)
print(todos[2])
print(todos[0:2])
medicos.append('Salvador')
print(medicos)

print("============================================================")

# COLEÇÕES - DICIONÁRIOS:
# Os dicionários representam coleções de dados que contém na sua estrutura um
# conjunto de pares chave/valor, nos quais cada chave individual tem um valor
# associado. Esse objeto representa a ideia de um mapa, que entendemos como
# uma coleção associativa desordenada. A associação nos dicionários é feita por
# meio de uma chave que faz referência a um valor.
# - del(dicionario)[elemento] – exclui elemento do dicionário
# - dicionario.items() – mostra todos itens do dicionário
# - dicionario.keys() – mostra todas as chaves do dicionário
# - dicionario.values() – mostra todos os valores das chaves do dicionário
# - dicionario.update(outro_dicionario) – concatena outro_dicionário em
# dicionario
medicos = {'Sandra': 'Dermatologista', 'Pablo': 'Traumatologista', 'Guilherme':
           'Cardiologista'}
print(medicos['Sandra'])
cliente = {'Nome': 'Luís Felipe Schilling',
           'Endereço': 'Rua Primeiro de Março, 113', 'Cidade': 'São Leopoldo'}
print(cliente)
print(cliente['Endereço'])
cliente['CEP'] = '93010-210'
print(cliente)
print(cliente.items())
print(cliente.keys())
print(cliente.values())
mais_dados = {'Estado': 'RS', 'País': 'Brasil'}
print(mais_dados)
print(cliente)
print(mais_dados)
cliente.update(mais_dados)
print(cliente)

for campo, valor in cliente.items():
    print(f'Nome do campo: {campo} Conteúdo: {valor}')

for campo, valor in cliente.items():
    print(f'{campo}: {valor}')

print("============================================================")

# COLEÇÕES – CONJUNTOS (SET):
# Em Python, um Set (conjunto) é uma coleção não-ordenada de valores únicos,
# empregada para armazenar múltiplos itens em um objeto.
# Algumas das principais características dos conjuntos incluem:
# • Armazena apenas itens não-duplicados (únicos)
# • Suporta operações matemáticas sobre conjuntos (união, intersecção, etc)
# • Não é possível modificar os itens existentes, mas podemos adicionar novos
# elementos (sets são mutáveis).
# • Suporta elementos de qualquer tipo, não-ordenados e não-indexados.
# • Podem conter apenas objetos imutáveis, como strings, ints, floats e tuplas de
# objetos também imutáveis.
# • São escritos com chaves.
conjunto = (1, 2, 3, 3, 7, 4, 6, 8, 3, 7)
print(conjunto)
print(set(conjunto))
c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}
c3 = c1.intersection(c2)
print(c1)
print(c2)
print(c3)
print(c1.difference(c2))
print(c2.difference(c1))

print("============================================================")
