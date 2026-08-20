# ENTRADA

odometro_inicio = float(input('Odômetro (KM); Início: '))
odometro_fim = float(input('Odômetro (KM); Final: '))

total_recebido = float(input('Total Recebido (R$): '))

combustivel_gasto = float(input('Combustível Utilizado (L): '))

PRECO_COMBUSTIVEL = 6.15

# PROCESSAMENTO

gastos_dia = combustivel_gasto * PRECO_COMBUSTIVEL
lucro_liquido = total_recebido - gastos_dia

kms_corridos = odometro_fim - odometro_inicio
media_kml = kms_corridos / combustivel_gasto

# SAÍDA

print(f'Lucro Líquido: R${lucro_liquido}')
print(f'Consumo Médio (KM/L): {media_kml}')