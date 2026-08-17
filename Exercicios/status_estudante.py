# ENTRADA

primeira_nota = 8
segunda_nota = 6.5
terceira_nota = 7
quarta_nota = 8.5

# PROCESSAMENTO

media = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4

if media > 7:
    status = "Aprovado!"
elif media >= 5:
    status = "Recuperação!"
else:
    status = "Reprovado!"

# SAÍDA

print(f'Situação: {status}')