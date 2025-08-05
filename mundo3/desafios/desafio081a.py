numeros = []
cont = 0

while True:

    num = int(input('Digite um valor: '))
    numeros.append(num)
    cont += 1

    while True:

        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        if resp in 'SN':
            break

    if resp == 'N':
        break

print(f'Você digitou {cont} elementos')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente são {numeros}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')