valores = list()

for n in range(0,5):
    valores.append(int(input(f'Digite um valor para a Posição {n}: ')))
print(f'Você digitou os valores {valores}')

posmax = posmin = ' '
for pos, valor in enumerate(valores):
    if valor == max(valores):
        posmax += str(pos) + '...'
    if valor == min(valores):
        posmin += str(pos) + '...'

print(f'O maior valor digitado foi {max(valores)} nas posições {posmax}')
print(f'O menor valor digitado foi {min(valores)} nas posições {posmin}')
