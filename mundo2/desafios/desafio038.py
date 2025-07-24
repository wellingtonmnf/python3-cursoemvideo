print('='*25)
print('COMPARADOR DE NÚMEROS')
print('='*25)

n1 = int(input('Digite o 1º número inteiro: '))
n2 = int(input('Digite o 2º número inteiro: '))

if n1 == n2:
    print('Não existe valor maior. Os números são iguais.')
elif n1 > n2:
    print(f'O valor {n1} é maior que {n2}')
else:
    print(f'O valor {n2} é maior que {n1}')