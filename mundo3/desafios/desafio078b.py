valores = list()

for n in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {n}: ')))
print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {max(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        print(f'{pos}...', end='')

print(f'\nO menor valor digitado foi {min(valores)} nas posições ',end='')
for pos, valor in enumerate(valores):
    if valor == min(valores):
        print(f'{pos}...', end='')
