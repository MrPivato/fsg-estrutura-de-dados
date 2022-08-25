# Crie um dicionário para armazenar os dados de um aluno.
# Os dados devem ser: Nome, Curso, Email, Telefone e RGM. Solicitar estes
# dados em uma estrutura de repetição. Imprimir estes valores ao final.

aluno = {"Nome": "", "Curso": "", "Email": "", "Telefone": "", "RGM": ""}
imprimir = ""

for k, _ in aluno.items():
    aluno[k] = input(f"Informe o {k} do aluno: ")
    imprimir += f"\n{k}: {aluno[k]}"

print(imprimir)