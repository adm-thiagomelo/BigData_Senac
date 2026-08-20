# ENTRADA

codigo_origem = int(input('Código de Origem: '))

# PROCESSAMENTO

match codigo_origem:
    case 1:
        origem = 'Sul'
    case 2:
        origem = 'Norte'
    case 3:
        origem = 'Leste'
    case 4:
        origem = 'Oeste'
    case 5:
        origem = 'Nordeste'
    case 6:
        origem = 'Nordeste'
    case 7:
        origem = 'Sudeste'
    case 8:
        origem = 'Sudeste'
    case 9:
        origem = 'Sudeste'
    case 10:
        origem = 'Centro-Oeste'
    case 11:
        origem = 'Noroeste'
    case _:
        origem = 'Importado'

# SAÍDA

print(f'Origem: {origem}')