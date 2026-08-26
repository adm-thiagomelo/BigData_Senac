candidatos_validos = []

for i in range(1,6):
    print(f'Candidato {i}')

    idade = int(input('Idade: '))

    if idade < 18:
        print('Rejeição')

        print()
    else:
        nome = input('Nome: ')
        email = input('E-mail: ')

        candidato = {'Nome': nome, 'E-mail': email}

        candidatos_validos.append(candidato)

        print()

print(candidatos_validos)
