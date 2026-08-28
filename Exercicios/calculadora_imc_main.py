import calculadora_imc

linha = '-' * 12

try:
    total_pessoas = int(input('Número de Pessoas: '))
except ValueError:
    print('Insira apenas números, por favor!')
    exit()

for i in range(1, total_pessoas + 1):
    print(linha)
    print(f'Candidato {i}')
    print(linha)

    try:
        altura = float(input('Altura: '))
        peso = float(input('Peso: '))
    except ValueError:
        print('Insira apenas números, por favor!')
        exit()

    print(linha)

    imc = calculadora_imc.calcular_imc(peso, altura)
    classificacao = calculadora_imc.obter_classificacao(imc)

    print(f'IMC: {imc:.2f}')
    print(f'Classificação: {classificacao}')
