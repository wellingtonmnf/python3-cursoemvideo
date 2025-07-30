resp = 'S'
soma = qtde = maior = menor = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    qtde += 1

    if qtde == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

media = float(soma / qtde)
print(f'Você digitou {qtde} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
