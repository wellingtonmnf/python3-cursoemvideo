print('-' * 40)
print(f'{" NÚMERO FATORIAL (N!) ":*^40}')
print('-' * 40)
n = int(input('Digite um número: '))
c = fat = n

for c in range(n, 1, -1):
    fat = fat * (c - 1)
print('-' * 40)
print(f'{n}! = {fat}')
