numeros = []

while True:

    num = int(input('Digite um valor: '))
    numeros.append(num)

    while True:

        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        if resp in 'SN':
            break

    if resp == 'N':
        break

print(f'Você digitou {len(numeros)} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista! ele está nas posições: ', end='')
    for pos, n in enumerate(numeros):
        if n == 5:
            print(pos + 1, end=' ')
else:
    print('O valor 5 não foi encontrado na lista!')
