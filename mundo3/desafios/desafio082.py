valores = []

while True:

    n = int(input('Digite um valor: '))
    valores.append(n)

    while True:

        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

        if resp not in 'SN':
            print('Tente novamente. ', end='')
        if resp in 'SN':
            break

    if resp == 'N':
        break

pares = []
impares = []

for valor in valores:
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
