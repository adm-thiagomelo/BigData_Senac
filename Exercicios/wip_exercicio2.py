# Cadastro Seletivo de Candidatos
# Use um for loop para iterar 5 vezes. Dentro do loop, use um if/else para checar se o
# candidato é menor de 18 anos (rejeição). Crie uma lista principal: candidatos_validos = [].
# Se o candidato for válido, crie um Dicionário (ex: candidato = {'nome': '...', 'email': '...'}).
# Adicione este Dicionário à lista: candidatos_validos.append(candidato)

candidatos_validos = []

for i in range(1, 6):
    print(f'Candidato {i}')

    idade = int(input('Idade: '))
    print()

    if idade < 18:
        print('Rejeição')
        print()
    else:
        imprimir_lista = True

        nome = input('Nome: ')
        email = input('Endereço Eletrônico: ')

        candidato = {'Nome': nome, 'Email': email}
        candidatos_validos.append(candidato)
        print()
