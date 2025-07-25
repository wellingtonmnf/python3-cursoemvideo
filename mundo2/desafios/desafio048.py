soma = 0
for c in range(1, 501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(f'{c} + ', end='')
            soma += c
print(f'= {soma}')
