num = list()
pares = list()
impares = list()
while True:
    num.append(int(input('Digite um número: ')))
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente  novamente. ', end='')
        else:
            break
    if resp == 'N':
        break
for i, v in enumerate(num): # Colocou um contador pro índice, porém não usou
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista dee ímpares é {impares}')
