def calculadora_v1(num1, num2, operacao = '1'):

    # num1 = float(input('Primeiro Dígito: '))
    # num2 = float(input('Segundo Dígito: '))
    # print('\n')

    # print('Qual é a operação que você gostaria de realizar?')
    # print('1. Adição')
    # print('2. Subtração')
    # print('3. Multiplicação')
    # print('4. Divisão')
    # print('\n')

    # operacao = input('R: ')
    # print('\n')

    match operacao:
        case '1':
            resultado = (f'Adição: {num1 + num2}')
        case '2':
            resultado = (f'Subtração: {num1 - num2}')
        case '3':
            resultado = (f'Multiplicação: {num1 * num2}')
        case '4':
            try:
                resultado = (f'Divisão: {num1 / num2}')
            except ZeroDivisionError:
                print('Não é possível dividir por zero.')
        case _:
            print('Operação inválida!')

    return resultado

calculinho = calculadora_v1(200, 100)

print(calculinho)
