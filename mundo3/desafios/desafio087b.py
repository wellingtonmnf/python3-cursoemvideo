matriz = [[], [], []]
pares = []
segunda_linha = []
soma_pares = soma_terceira_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = int(input(f'Digite o {coluna + 1}º valor da {linha + 1}º linha: '))
        matriz[linha].append(n)
        
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        elemento = matriz[linha][coluna]

        print(f'[ {elemento} ]', end='')

        if elemento % 2 == 0:
            pares.append(elemento)
            soma_pares += elemento
        if coluna == 2:
            soma_terceira_coluna += elemento
        if linha == 1:
            segunda_linha.append(elemento)
    print()

print(f'A soma dos valores pares {pares} é igual a {soma_pares}')
print(f'A soma dos valores da 3ª coluna é igual a {soma_terceira_coluna}')
print(f'O maior valor da 2ª linha é igual a {max(segunda_linha)}')
