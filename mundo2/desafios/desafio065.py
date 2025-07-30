print('-' * 30)
print(f'{" ANALISADOR DE NÚMEROS ":^30}')
print('-' * 30)

resp = 'S'
cont = soma = maior = menor = 0

while resp == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n

    resp = str(input('Quer continuar a digitar valores? [S/N]')).upper().strip()
    print('-' * 30)

media = float(soma / cont)

print('RELATÓRIO')
print(f'MÉDIA: {media:.2f}')
print(f'MAIOR: {maior}')
print(f'MENOR: {menor}')
