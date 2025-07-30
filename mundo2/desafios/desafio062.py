termo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA:'))
c = n = 1
print('-' * 40)

while c <= 10:
    print(termo, end=' ➞ ')
    termo += razao
    c += 1
print('FIM DOS DEZ PRIMEIROS TERMOS')

while n != 0:
    print()
    print('-' * 40)
    n = int(input('Deseja ver mais quantos termos? [0 = SAIR]: '))
    print('-' * 40)
    if n != 0:
        c = 1
        while c <= n:
            print(termo, end=' ➞ ')
            termo += razao
            c += 1

print('FIM DO PROGRAMA')
