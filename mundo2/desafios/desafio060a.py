print('-' * 40)
print(f'{" FATORIAL DE UM NÚMERO (N!) ":*^40}')
print('-' * 40)
n = int(input('Digite um número: '))
c = fat = n

while c > 1:
    fat = fat * (c - 1)
    c -= 1
print('-' * 40)
print(f'{n}! = {fat}')