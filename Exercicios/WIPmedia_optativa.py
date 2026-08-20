# ENTRADA

nota_um = int(input('Primeira Nota: '))
nota_dois = int(input('Segunda Nota:'))
nota_optativa = int(input('Nota da Optativa: '))

# PROCESSAMENTO

# Necessário rever processamento.

# if nota_optativa > nota_um > nota_dois:
#     nota_dois = nota_optativa
# elif nota_optativa > nota_dois > nota_um:
#     nota_um = nota_optativa
# elif nota_um > nota_optativa > nota_dois:
#     nota_dois = nota_optativa
# elif nota_dois > nota_optativa > nota_um:
#     nota_um = nota_optativa

media = (nota_um + nota_dois) / 2

# SAÍDA

print(f'Média: {media}')