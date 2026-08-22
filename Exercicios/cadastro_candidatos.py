ano_presente = 2026

for num_candidato in range(1, 13):
    print(f'Candidato {num_candidato}')

    ano_nascimento = int(input('Ano de Nascimento: '))    
    idade = ano_presente - ano_nascimento

    if idade >= 18:
        telefone = input('Telefone: ')
        email = input('Correio Eletrônico: ')
    else:
        print('Sua idade é insuficiente!')

    print('')
    print('')