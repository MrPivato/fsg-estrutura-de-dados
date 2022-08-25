# Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos, 
# fazendo a leitura dos valores por meio de uma estrutura de repetição. 
# Depois, crie uma nova estrutura de repetição para somar todas as notas e 
# retornar a média.

alunos = {}
NUM_ALUNOS = 3

for i in range(NUM_ALUNOS):
    nome = input(f"Digite o nome do {i+1}° aluno: ")
    nota = float(input(f"Digite a nota do {i+1}° aluno: "))
    alunos[nome] = nota

media = 0
for i, v in alunos.items():
    media += v

media /= NUM_ALUNOS

print(f"\nMédia dos alunos da classe é: {media}")



# pode se fazer assim tbm
# alunos[input(f"Digite o nome do {i+1}° aluno: ")] = float(input(f"Digite a nota do {i+1}° aluno: "))
