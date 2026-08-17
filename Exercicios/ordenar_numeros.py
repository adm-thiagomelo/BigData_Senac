# ENTRADA

primeiro_valor = int(input('Primeiro Valor: '))
segundo_valor = int(input('Segundo Valor: '))
terceiro_valor = int(input('Terceiro Valor: '))

# PROCESSAMENTO

# A voz na minha cabeça me diz que esse código está redundante... que dá pra ser mais eficiente, mais enxuto!

if primeiro_valor > segundo_valor and primeiro_valor > terceiro_valor:
    valor_maior = primeiro_valor

    if segundo_valor > terceiro_valor:
        valor_meio = segundo_valor
        valor_menor = terceiro_valor
    else:
        valor_meio = terceiro_valor
        valor_menor = segundo_valor

elif primeiro_valor > segundo_valor and primeiro_valor < terceiro_valor:
    valor_maior = terceiro_valor
    valor_meio = primeiro_valor
    valor_menor = segundo_valor

elif primeiro_valor < segundo_valor and primeiro_valor > terceiro_valor:
    valor_maior = segundo_valor
    valor_meio = primeiro_valor
    valor_menor = terceiro_valor

elif primeiro_valor < segundo_valor and primeiro_valor < terceiro_valor:
    valor_menor = primeiro_valor

    if segundo_valor > terceiro_valor:
        valor_maior = segundo_valor
        valor_meio = terceiro_valor
    else:
        valor_maior = terceiro_valor
        valor_meio = segundo_valor

# SAÍDA

print(f'Menor: {valor_menor}')
print(f'Meio: {valor_meio}')
print(f'Maior: {valor_maior}')