lever = 1

# while lever <= 5:
#     print(f'Entrada ({lever}/5)')
#     num = float(input('Número: '))

#     print(f'Dobro: {num * 2}')
#     print(f'Triplo: {num * 3}')

#     lever += 1



# for i in range(1, 6):
#     print(f'Entrada ({i}/5)')
#     num = float(input('Número: '))

#     print(f'Dobro: {num * 2}')
#     print(f'Triplo: {num * 3}')



while True:
    if lever > 5:
        break

    print(f'Entrada ({lever}/5)')
    num = float(input('Número: '))

    print(f'Dobro: {num * 2}')
    print(f'Triplo: {num * 3}')

    lever += 1

print('Fim.')