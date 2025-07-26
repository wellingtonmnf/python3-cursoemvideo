soma, cont = 0, 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} números ímpares que são múltiplos de 3,\nno intervalo entre 1 e 500, é igual a {soma}')
