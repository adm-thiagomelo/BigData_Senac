# 1. Cálculo de Lâmpadas:
# Escreva um programa para calcular e imprimir o número de lâmpadas necessárias para
# iluminar um determinado cômodo de uma residência. Dados de entrada: a potência da
# lâmpada utilizada (em watts), as dimensões (largura e comprimento, em metros) do
# cômodo. Considere que a potência necessária é de 3 watts por metro quadrado e a cada
# 3m² existe um bocal para uma lâmpada.

# ENTRADA

potencia = float(input('Potência da Lâmpada (W): '))
largura = float(input('Largura do Cômodo (M): '))
comprimento = float(input('Comprimento do Cômodo (M): '))

# PROCESSAMENTO

comodo_m2 = largura * comprimento
watts_necessarios = comodo_m2 * 3 # ("a potência necessária é de 3 watts por metro quadrado")
lampadas_necessarias = watts_necessarios / potencia
num_bocais = comodo_m2 / 3 # ("a cada 3m² existe um bocal para uma lâmpada")

# SAÍDA

if lampadas_necessarias <= num_bocais:
    print(f'São necessárias {lampadas_necessarias} lâmpadas para iluminar esse cômodo.')
else:
    print(f'Não é possível iluminar o cômodo com esses parâmetros.')
