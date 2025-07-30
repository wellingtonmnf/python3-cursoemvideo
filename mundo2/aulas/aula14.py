'''for c in range(1,10):
    print(c)
print('Fim')'''

c = 1
while c < 10:
    print(c)
    c += 1
print('Fim')

'''for c in range(1, 5):
    n = int(input('Digite um valor: '))
print('Fim')'''

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')

n = 1
pares = impares = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
print(f'Você digitou {pares} números pares e {impares} números ímpares.')
