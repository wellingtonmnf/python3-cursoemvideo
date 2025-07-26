# Solução nº 1 (com duas iterações)
for n in range(1, 51):
    print('.', end='')
    if n % 2 == 0:
        print(n, end=' ')
print('Acabou')
# Solução nº 2 (com uma iteração)
for n in range(2, 51, 2):
    print('.', end='')
    print(n, end=' ')
print('Acabou')

# Quanto menos iterações, melhor o desempenho
