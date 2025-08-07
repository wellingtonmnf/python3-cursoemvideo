matriz = [[], [], []]
pares = []
soma_pares = soma_terceira_coluna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite o {coluna + 1}º valor da {linha + 1}º linha: '))
        if n % 2 == 0:
            pares.append(n)
            soma_pares += n
        matriz[linha].append(n)
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[ {matriz[linha][coluna]} ]', end='')
    print()

for c in range(0, 3):
    if matriz[c][2]:
        soma_terceira_coluna += matriz[c][2]
    if matriz[1][c]:
        if c == 0:
            maior = matriz[1][c]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]


print(f'A soma dos valores pares {pares} é igual a {soma_pares}')
print(f'A soma dos valores da 3ª coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor da 2ª linha é igual a {maior}')
