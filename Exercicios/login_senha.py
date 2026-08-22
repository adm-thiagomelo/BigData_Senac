# 3. Tentativa de Login e Senha
# Simule um sistema de login simples onde o usuário tem um número limitado de tentativas
# para digitar a senha correta.
# ● Defina um nome de usuário e uma senha corretos (ex: admin e 123456).
# ● Dê ao usuário 3 tentativas para acertar a combinação.
# ● Se a senha estiver correta, imprima uma mensagem de sucesso e use o comando
# break para sair do loop.
# ● Se a senha estiver errada, informe o erro e diminua o número de tentativas
# restantes.
# ● Se as tentativas acabarem, imprima uma mensagem de bloqueio

# usar for


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
        print('Bem-vindo, Douglas!')
        break
    else:
        print('Usuário ou senha incorretos!')
        print()

if login != login_correto and senha != senha_correta:
    print('Bloqueio!')
