def calcular_imc(peso, altura):
    '''
    Recebe o peso e a altura para calcular o Índice de Massa Corporal (IMC).
    '''

    imc = peso / (altura * altura)

    return imc

def obter_classificacao(imc):
    '''
    Determina, a partir do Índice de Massa Corporal (IMC) se o indivíduo está em situação
    de obesidade, sobrepeso, normal ou abaixo do peso.
    '''

    if imc >= 30:
        classificacao = 'Obesidade'
    elif imc >= 25:
        classificacao = 'Sobrepeso'
    elif imc >= 18.5:
        classificacao = 'Normal'
    else:
        classificacao = 'Abaixo do Peso'

    return classificacao
