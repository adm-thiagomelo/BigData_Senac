# ENTRADA

nota_um = int(input('Primeira Nota: '))
nota_dois = int(input('Segunda Nota:'))
nota_optativa = int(input('Nota da Optativa: '))

# PROCESSAMENTO

if nota_optativa != -1:

    if nota_um > nota_dois and nota_optativa > nota_dois:
        nota_dois = nota_optativa        
    elif nota_um == nota_dois and nota_optativa > nota_um:
        nota_um = nota_optativa
        # nota_dois = nota_optativa     # Equivalente.
    elif nota_um < nota_dois and nota_optativa > nota_um:
        nota_um = nota_optativa

    media = (nota_um + nota_dois) / 2

else:
    media = (nota_um + nota_dois) / 2

if media >= 6:
    situacao = "Aprovação!"
elif media >= 3 and media < 6:
    situacao = "Recuperação!"
else:
    situacao = "Reprovação!"


# SAÍDA

print(f'Média: {media}')
print(f'Situação: {situacao}')