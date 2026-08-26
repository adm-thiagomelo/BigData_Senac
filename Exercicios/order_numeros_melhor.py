lista_nums = []

# ENTRADA

num1 = float(input('Primeiro Número: '))
num2 = float(input('Segundo Número: '))
num3 = float(input('Terceiro Número:'))

# PROCESSAMENTO

lista_nums.append(num1)
lista_nums.append(num2)
lista_nums.append(num3)

lista_nums.sort()

# SAÍDA

print(f'Maior: {lista_nums[2]}')
print(f'Mediano: {lista_nums[1]}')
print(f'Menor: {lista_nums[0]}')
