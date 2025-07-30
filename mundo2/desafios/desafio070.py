print('-' * 50)
print(f'{"LOJA SUPER BARATÃO":^50}')
print('-' * 50)

total = caros = cont = 0

while True:
    nome = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    cont += 1

    total += preco

    if preco > 1000:
        caros += 1

    if cont == 1:
        precomaisbarato = preco
        nomemaisbarato = nome
    else:
        if preco < precomaisbarato:
            precomaisbarato = preco
            nomemaisbarato = nome

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SsNn':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'{" FIM DO PROGRAMA ":-^50}')
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {caros} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {nomemaisbarato} que custa R$ {precomaisbarato:.2f}')
