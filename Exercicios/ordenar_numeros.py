# ENTRADA

num1 = float(input('Entrada 1: '))
num2 = float(input('Entrada 2: '))
num3 = float(input('Entrada 3: '))

# PROCESSAMENTO

# Atualização: Estive muito insatisfeito com a lógica da análise combinatória. Há muitos cenários
# possíveis. Em razão disso, o código tornou-se extenso. Então, decidi buscar sugestões da inteligência
# artificial para otimizar esse processo. O seguinte código é resultado disso:

if num1 > num2:
    num1, num2 = num2, num1

if num2 > num3:
    num2, num3 = num3, num2

if num1 > num2:
    num1, num2 = num2, num1

# SAÍDA

print(f'R: {num1}, {num2} e {num3}')
