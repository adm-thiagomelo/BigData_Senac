# ENTRADA

odometro_inicio = float(input('Odômetro (KM); Início: '))
odometro_fim = float(input('Odômetro (KM); Final: '))

combustivel_gasto = float(int(input('Combustível (L): ')))

total_recebido = float(int(input('Total Recebido (R$): ')))

PRECO_COMBUSTIVEL = 6.15



# PROCESSAMENTO

kms_corridos = odometro_fim - odometro_inicio
custo_dia = combustivel_gasto * PRECO_COMBUSTIVEL
lucro_liquido = total_recebido - custo_dia

# SAÍDA

print(f'Lucro Líquido (R$): R${lucro_liquido}')