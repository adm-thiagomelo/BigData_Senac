# ENTRADA

num1 = float(input('Entrada 1: '))
num2 = float(input('Entrada 2: '))
num3 = float(input('Entrada 3: '))

# PROCESSAMENTO

# Atualização: O código tornou-se demasiadamente extenso ao tentar atender cada cenário possível. Em razão da minha insatisfação,
# busquei por sugestões da inteligência artificial para otimizar esse processo. Para fins comparativos, o versionamento foi
# realizado.

if num1 > num2:
    num1, num2 = num2, num1

if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1

# SAÍDA

print(f'R: {num1}, {num2} e {num3}')
