n = int(input('Digite um número para\ncalcular seu Fatorial: '))
#c = n
fat = 1
print(f'Calculando {n}!', end=' = ')

for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    fat *= c
print(fat)