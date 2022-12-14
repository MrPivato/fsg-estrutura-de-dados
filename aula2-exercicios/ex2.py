# Calcular a média de um aluno que cursou a disciplina de Estrutura de Dados, a
# partir da leitura das notas A1 e A2. Calcular a Nota Final (NF) com base na
# soma de A1 com A2. Caso NF seja inferior a 6,0, solicitar a nota de Avaliação
# Final (AF), e calcular a nota NF, com base em AF somado a maior entre A1 e
# A2. Solicitar também o percentual de presença (PP). Após a NF calculada,
# devemos anunciar se o aluno o resultado final do aluno.
# - Se a soma entre A1 e A2 for superior a 6,0 e PP superior ou igual a 75 %, o
# aluno está ‘Aprovado sem Avaliação Final’;
# - Se a soma entre o maior entre A1 e A2 com AF for superior ou igual a 6,0 e
# PP superior ou igual a 75 %, o aluno está ‘Aprovado com Avaliação Final’;
# - Se a soma entre o maior entre A1 e A2 com AF for inferior a 6,0 e PP superior
# ou igual a 75 %, o aluno está ‘Reprovado por nota insuficiente’;
# - Se PP for inferior a 75% o aluno está ‘Reprovado por frequencia inferior a
# 75%’.

A1, A2, NF, PP, media = 0.0, 0.0, 0.0, 0.0, 0.0

PP = float(input("Informe seu percentual de Presença (%): "))

if PP < 75.0:
    print("Reprovado por frequencia inferior a 75%")
else:
    A1 = float(input("Informe sua nota A1: "))
    A2 = float(input("Informe sua nota A2: "))
    NF = A1 + A2

    if NF < 6.0:
        print("Sua nota foi inferior a 6, por favor realize a AF.")
        AF = float(input("Informe sua nota AF: "))
        if A1 > A2:
            NF = A1 + AF
        else:
            NF = A2 + AF

        if NF < 6.0:
            print(f"Aluno REPROVADO com nota: {NF}")
        else:
            print(f"Aluno APROVADO com nota: {NF}")
    else:
        print(f"Aluno APROVADO com nota: {NF}")
