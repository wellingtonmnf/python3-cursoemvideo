numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        r = str(input('Quer continuar? [S/N}: ')).strip().upper()[0]
        if r not in 'SN':
            print('Tente novamente. ', end='')
        else:
            break
    if r == 'N':
        break
print('-=' * 30)
numeros.sort()
print(f'Você digitou os valores {numeros}')
