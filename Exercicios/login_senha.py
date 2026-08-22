login_correto = 'douglas'
senha_correta = 'abobora'

# ENTRADA

for tentativa in range(1, 4):
    print(f'Tentativa ({tentativa}/3)')
    print()

    login = input('Login: ')
    senha = input('Senha: ')
    print()

    if login == login_correto and senha == senha_correta:
        bloqueio = 'off'

        print('Bem-vindo, Douglas!')
        break
    else:
        bloqueio = 'on'

        print('Usuário ou senha incorretos!')
        print()

if bloqueio == 'on':
    print('Bloqueio!')
