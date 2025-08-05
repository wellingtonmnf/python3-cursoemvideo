valores = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp not in 'SN':
            print('Tente novamente.', end=' ')
        if resp in 'SN':
            break

    if resp == 'N':
        break

valores.sort()  # Ordena a lista original
print('-=' * 30)
print(f'Você digitou os valores {valores}')
