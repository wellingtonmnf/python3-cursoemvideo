matriz = [[], [], []]

for c in range(0, 3):
    for i in range(0, 3):
        n = int(input(f'Digite o {i + 1}º valor da {c + 1}º linha: '))
        matriz[c].insert(i, n)
print('-' * 30)
for c in range(0, 3):
    for i in range(0, 3):
        print(f'[ {matriz[c][i]:^3} ]', end='')
    print()
