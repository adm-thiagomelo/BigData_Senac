# ENTRADA

preco_combustivel = 6.15

odometro_inicio = float(input('Odômetro (KM); Início do Dia: '))
odometro_fim = float(input('Odômetro (KM); Final do Dia: '))

combustivel_gasto = float(input('Combustível Gasto (L): '))

total_recebido = float(input('Total Recebido (R$): '))

# PROCESSAMENTO

# Média do consumo em KM/L.

km_rodados = odometro_fim - odometro_inicio
