# 2. Cadastro de Candidatos
# Desenvolva um programa que colete dados de 12 pessoas, usando a decisão para filtrar
# candidatos menores de 18 anos.
# ● O programa deve pedir o Ano de Nascimento do candidato.
# ● Se for menor de 18, o programa deve informar que ele não pode participar e pular
# a coleta dos demais dados (telefone, email etc) para esse candidato.
# ● Se for maior de 18, o programa prossegue com o input() para os demais dados.

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