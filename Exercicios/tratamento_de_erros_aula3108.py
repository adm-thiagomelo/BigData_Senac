try:
    int(input('Insira um número inteiro: '))
except ValueError:
    print('Você inseriu um dado inválido.')
finally:
    print('Sucesso.')