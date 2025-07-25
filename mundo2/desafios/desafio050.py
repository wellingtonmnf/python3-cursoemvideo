print('+' * 20)
print(f'{"SOMADOR DE PARES":=^20}')
print('+' * 20)

soma = 0
pares = []

for c in range(1, 7):
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0:
        print(f'{n} é PAR')
        pares += [n]
        soma += n

print(f'Números pares digitados: {pares}')
print(f'Soma dos números pares: {soma}')
