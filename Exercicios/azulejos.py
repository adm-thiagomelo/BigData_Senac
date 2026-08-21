# ENTRADA

comprimento = float(input('Comprimento (M): '))
largura = float(input('Largura (M): '))
altura = float(input('Altura (M): '))

CAIXA_AZULEJOS_M2 = 1.5

# PROCESSAMENTO E SAÍDA

if comprimento > 0 and largura > 0 and altura > 0:
    comprimento_m2 = (comprimento * altura) * 2
    largura_m2 = (largura * altura) * 2
    parede_total = comprimento_m2 + largura_m2

    caixas_necessarias = parede_total / CAIXA_AZULEJOS_M2

    print(f'Caixas Necessárias: {caixas_necessarias}')
else:
    print('Os dados inseridos são inválidos! Por favor, insira apenas valores numéricos que sejam maiores do que zero.')