resultados = []

for estudante in range(1, 6):
    print(f'Aluno {estudante}')

    nota_um = float(input('Primeira Nota: '))
    nota_dois = float(input('Segunda Nota: '))

    media = (nota_um + nota_dois) / 2

    if media >= 6:
        situacao = "Aprovação"
    elif 3 <= media < 6:
        situacao = "Recuperação"
    else:
        situacao = "Reprovação"

    print()

    resultados.append(f'Aluno {estudante} - {situacao}')

print(resultados)
 