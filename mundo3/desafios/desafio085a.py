pares = []
impares = []
numeros = [pares, impares]

for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'Os valores digitados foram: {numeros}')
pares.sort()
impares.sort()
print('-' * 30)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores ímpares digitados foram: {impares}')
