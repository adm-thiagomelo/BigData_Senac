for cada_estudante in range(1, 11):
    print(f'Estudante {cada_estudante}')
    primeira_nota = float(input('Primeira Nota: '))
    segunda_nota = float(input('Segunda Nota: '))
    nota_optativa = float(input('Optativa: '))

    if nota_optativa != -1 and (nota_optativa > primeira_nota or nota_optativa > segunda_nota):
        if primeira_nota > segunda_nota:
            segunda_nota = nota_optativa
        else: # segunda_nota > primeira_nota
            primeira_nota = nota_optativa

    media = (primeira_nota + segunda_nota) / 2

    if media >= 6:
        status = 'Aprovação'
    elif 3 <= media < 6:
        status = 'Recuperação'
    else:
        status = 'Reprovação'

    print(f'Média: {media}')
    print(f'Situação: {status}')
    print('')
    print('')
