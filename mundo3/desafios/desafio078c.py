valores, posmax, posmin = [], [], []

for c in range(0, 5):
    n = int(input(f'Digite um valor para a Posição {c}: '))
    valores.append(n)
print('-=' * 30)
print(f'Você digitou os valores {valores}')
for pos, valor in enumerate(valores):
    if valor == max(valores):
        posmax.append(pos)
    if valor == min(valores):
        posmin.append(pos)
print(f'O maior valor digitado foi {max(valores)} nas posições: {posmax}')
print(f'O menor valor digitado foi {min(valores)} nas posições: {posmin}')
